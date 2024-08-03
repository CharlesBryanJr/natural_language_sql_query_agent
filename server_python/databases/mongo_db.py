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

import os
import json
import openai
import pymongo
from pymongo.errors import ConnectionFailure
from bson import ObjectId
import numpy as np
from urllib.parse import quote_plus
from dotenv import load_dotenv, find_dotenv

os.environ.pop('OPENAI_API_KEY', None)
dotenv_path = '/Users/charlesbryan/Desktop/natural_language_sql_query_agent/.env'
if dotenv_path:
    load_dotenv(dotenv_path)
else:
    print("Error: .env file not found")

api_key = os.getenv('OPENAI_API_KEY')

# from find_joins import data


class MongoVectorDatabase:
    def __init__(self,
                 mongo_connection_string="mongodb+srv://charlesabryanjr:MBcab312.jr02mb@cluster0.tsdcnth.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
                 db_name="aws_open_data_registry",
                 collection_name="covid-19",
                 openai_api_key=os.getenv("OPENAI_API_KEY")
                ):
        print(f'MongoVectorDatabase')
        self.client = pymongo.MongoClient(mongo_connection_string)
        self.db = self.client[db_name]
        self.collection_name = collection_name
        self.collection = self.db[collection_name]
        self.openai_api_key = openai_api_key

        if collection_name not in self.db.list_collection_names():
            self.db.create_collection(collection_name)

    def database_exists(self, database_name="aws_open_data_registry"):
        if database_name is None:
            raise ValueError("Database name cannot be None")
        return database_name in self.client.list_database_names()

    def collection_exists(self, collection_name="covid-19"):
        if collection_name is None:
            collection_name = self.collection_name
        return collection_name in self.db.list_collection_names()

    def get_embedding(self, text):
        print(f'get_embedding')
        try:
            response = openai.embeddings.create(
                input=text,
                model="text-embedding-ada-002"
            )
            return response.data[0].embedding
        except openai.BadRequestError as e:
            print(f"Error: {e}")
            raise

    def add_to_vector_db(self, data_dict):
        print(f'add_to_vector_db')
        documents = []
        for key, value in data_dict.items():
            existing_doc = self.collection.find_one({"table": key})
            if existing_doc:
                print(f"Document with table '{key}' already exists. Skipping.")
                continue

            document_str = json.dumps(value, cls=MongoJSONEncoder)
            embedding = self.get_embedding(document_str)
            document = {
                "_id": ObjectId(),
                "table": key,
                "columns": value["columns"],
                "joins": value["joins"],
                "description": value["description"],
                "embedding": embedding
            }
            documents.append(document)
        if documents:
            self.collection.insert_many(documents)

    def query_vector_db(self, query, n_results=3):
        print(f'query_vector_db')
        print(f'query - {query}')
        query_embedding = self.get_embedding(query)
        documents = list(self.collection.find({}, {"embedding": 1, "table": 1, "columns": 1, "description": 1}))
        embeddings = np.array([doc['embedding'] for doc in documents])

        distances = np.linalg.norm(embeddings - query_embedding, axis=1)
        indices = np.argsort(distances)[:n_results]

        # results = [documents[i] for i in indices]
        results = [{
            'table': str(documents[i]['table']),
            'columns': documents[i].get('columns', None),
            'description': documents[i].get('description', None)
        } for i in indices]
        return results
    
    def print_dataset_info(self, dataset_info):
        for dataset in dataset_info:
            print("[{")
            print(f"    'table': '{dataset['table']}',")
            print(f"    'columns': {dataset['columns']},")
            print(f"    'description': '{dataset['description']}'")
            print("}]")


class MongoJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)

'''
if __name__ == "__main__":
    db = MongoVectorDatabase()
    db.add_to_vector_db(data)
    query = "write a SQL query calculates the total number of COVID-19 tests conducted in each state and then lists these states in descending order based on the volume of tests, starting with the state that has conducted the most tests."
    results = db.query_vector_db(query, n_results=1)
    print(results)
    print('-'*30)
'''