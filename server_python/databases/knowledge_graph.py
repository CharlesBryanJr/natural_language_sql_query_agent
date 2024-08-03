# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0121
# pylint: disable=E0401
# pylint: disable=C0413
# pylint: disable=C0411
# pylint: disable=W0611
# pylint: disable=W1309
# pylint: disable=W0621
# pylint: disable=C0301
# pylint: disable=C0303

import os
import json
import openai
from neo4j import GraphDatabase
import numpy as np
from dotenv import load_dotenv, find_dotenv

os.environ.pop('OPENAI_API_KEY', None)
dotenv_path = '/Users/charlesbryan/Desktop/natural_language_sql_query_agent/.env'
if dotenv_path:
    load_dotenv(dotenv_path)
else:
    print("Error: .env file not found")

api_key = os.getenv('OPENAI_API_KEY')

# from databases.find_joins import data

class KnowledgeGraph:
    def __init__(self, uri="neo4j+s://dd8a283a.databases.neo4j.io:7687", user="neo4j", password="AygF7sLwBp3OLU0y2zhqYPHTgqP4RdYaNJtOXP3bSOE"):
        print(f'KnowledgeGraph')
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        print(f'close')
        self.driver.close()

    def add_tables_columns_and_joins(self, data):
        print(f'add_tables_columns_and_joins')
        with self.driver.session() as session:
            for table_name, table_info in data.items():
                session.run("MERGE (:Table {name: $name, description: $description})", 
                            name=table_name, description=table_info.get('description', ''))
                
                for column in table_info.get('columns', []):
                    session.run("""
                        MATCH (t:Table {name: $table_name})
                        MERGE (c:Column {name: $column_name})
                        MERGE (t)-[:HAS_COLUMN]->(c)
                    """, table_name=table_name, column_name=column)
                
                # Create joins through columns
                for join in table_info.get('joins', []):
                    join_table = join['table']
                    join_column = join['column']
                    session.run("""
                        MATCH (t1:Table {name: $table_name})-[:HAS_COLUMN]->(c:Column {name: $join_column}),
                            (t2:Table {name: $join_table})-[:HAS_COLUMN]->(c)
                        MERGE (t1)-[:JOINS_ON]->(c)
                        MERGE (t2)-[:JOINS_ON]->(c)
                    """, table_name=table_name, join_table=join_table, join_column=join_column)

    def get_schema_overview(self):
        print(f'get_schema_overview')
        with self.driver.session() as session:
            result = session.run("""
                MATCH (t:Table)
                OPTIONAL MATCH (t)-[:HAS_COLUMN]->(c:Column)
                RETURN t.name as name, t.description as description, collect(c.name) as columns
            """)
            return {record["name"]: {'description': record["description"], 'columns': record["columns"]} for record in result}

    def create_table_embeddings(self):
        print(f'create_table_embeddings')
        schema = self.get_schema_overview()
        texts = []
        table_names = []
        for table, info in schema.items():
            text = table + ' ' + info['description'] + ' ' + ' '.join(info['columns'])
            texts.append(text)
            table_names.append(table)
        
        embeddings = self.get_openai_embeddings(texts)
        return embeddings, table_names

    def get_openai_embeddings(self, texts):
        print(f'get_openai_embeddings')
        embeddings = []
        for text in texts:
            response = openai.embeddings.create(input=text, model="text-embedding-ada-002")
            embeddings.append(response.data[0].embedding)
        return embeddings

    def store_embeddings_in_neo4j(self):
        print(f'store_embeddings_in_neo4j')
        embeddings, table_names = self.create_table_embeddings()
        with self.driver.session() as session:
            for table, embedding in zip(table_names, embeddings):
                session.run("""
                    MATCH (t:Table {name: $table})
                    SET t.embedding = $embedding
                """, table=table, embedding=embedding)

    def get_table_embeddings(self):
        print(f'get_table_embeddings')
        with self.driver.session() as session:
            result = session.run("""
                MATCH (t:Table)
                RETURN t.name as name, t.embedding as embedding
            """)
            embeddings = []
            table_names = []
            for record in result:
                embeddings.append(np.array(record["embedding"]))
                table_names.append(record["name"])
            return np.array(embeddings), table_names

    def identify_relevant_tables(self, query, n_results=3):
        print(f'identify_relevant_tables')
        query_embedding = self.get_openai_embeddings([query])[0]
        table_embeddings, table_names = self.get_table_embeddings()
        
        distances = np.linalg.norm(table_embeddings - query_embedding, axis=1)
        nearest_indices = distances.argsort()[:n_results]
        relevant_tables = [table_names[idx] for idx in nearest_indices]
        
        return relevant_tables

    def get_column_info(self, tables):
        print(f'get_column_info')
        with self.driver.session() as session:
            result = session.run("""
                MATCH (t:Table)-[:HAS_COLUMN]->(c:Column)
                WHERE t.name IN $tables
                RETURN t.name as table, collect(c.name) as columns
            """, tables=tables)
            return {record["table"]: record["columns"] for record in result}

    def find_join_paths(self, relevant_tables, max_depth=1):
        print(f'find_join_paths')
        if len(relevant_tables) < 2:
            print("Not enough tables for a join path.")
            return []

        query = f"""
            MATCH (start:Table)
            WHERE start.name IN $tables
            CALL {{
                WITH start
                MATCH path = (start)-[:HAS_COLUMN]->(c:Column)<-[:HAS_COLUMN]-(end:Table)
                WHERE end.name IN $tables AND end.name > start.name
                RETURN path
            }}
            RETURN 
                [node IN nodes(path) | node.name] AS table_path,
                [rel IN relationships(path) | type(rel) + ': ' +
                    startNode(rel).name + ' -> ' +
                    endNode(rel).name] AS join_conditions
        """

        with self.driver.session() as session:
            result = session.run(query, tables=relevant_tables)
            paths = [{"path": record["table_path"], "joins": record["join_conditions"]}
                    for record in result]

        if not paths:
            print("No join paths found.")
            return paths

        for i, path in enumerate(paths, 1):
            print(f"\nPath {i}:")
            print("  Tables in path: " + " -> ".join(path['path']))
            print("  Join conditions:")
            for join in path['joins']:
                print("    - " + join)

        return paths


    def suggest_aggregations(self, query, columns):
        print(f'suggest_aggregations')
        agg_keywords = {
            'sum': ['total', 'sum', 'amount'],
            'avg': ['average', 'mean'],
            'count': ['number of', 'count', 'how many'],
            'max': ['maximum', 'highest', 'top'],
            'min': ['minimum', 'lowest', 'bottom']
        }
        suggestions = []
        for agg, keywords in agg_keywords.items():
            if any(keyword in query.lower() for keyword in keywords):
                suggestions.extend([f"{agg}({col})" for col in columns if col.lower() in query.lower()])
        return suggestions

    def assist_sql_translation(self, natural_language_query):
        print(f'assist_sql_translation')
        self.store_embeddings_in_neo4j()
        relevant_tables = self.identify_relevant_tables(natural_language_query)
        column_info = self.get_column_info(relevant_tables)
        join_paths = self.find_join_paths(relevant_tables) if len(relevant_tables) > 1 else []
        all_columns = [col for cols in column_info.values() for col in cols]
        suggested_aggregations = self.suggest_aggregations(natural_language_query, all_columns)
        
        translation_assist = {
            'relevant_tables': relevant_tables,
            'column_info': column_info,
            'join_paths': join_paths,
            'suggested_aggregations': suggested_aggregations
        }
        
        return translation_assist

"""
if __name__ == "__main__":
    kg = KnowledgeGraph()
    #kg.add_tables_columns_and_joins(data)
    
    nl_query = "write a SQL query calculates the total number of COVID-19 tests conducted in each state and then lists these states in descending order based on the volume of tests, starting with the state that has conducted the most tests."
    assistance = kg.assist_sql_translation(nl_query)
    
    print("Assistance for SQL Translation:")
    print(f"Relevant Tables: {assistance['relevant_tables']}")
    print(f"Column Info: {assistance['column_info']}")
    print('-'*30)
    print('-'*30)
    print('-'*30)
    print(f"Suggested Join Paths: {assistance['join_paths']}")
    #print(f"Suggested Aggregations: {assistance['suggested_aggregations']}")
    
    kg.close()
"""