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

import warnings
warnings.filterwarnings("ignore")
import os
import re
from typing import List, Dict, Any, TypedDict
from typing_extensions import TypedDict
import openai
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage, ToolMessage, AIMessage
from langchain_core.pydantic_v1 import BaseModel
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph, MessagesState
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.checkpoint.aiosqlite import AsyncSqliteSaver

from api.athena_operations import execute_athena_query_function
from databases.mongo_db import MongoVectorDatabase
from databases.knowledge_graph import KnowledgeGraph


from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

# Assuming get_table_names and get_database_schemas functions are defined in get_table_schema.py
from get_table_schema import get_table_names, get_database_schemas

class AgentState(TypedDict):
    query: str
    database: str
    review_define_objective: bool
    review_before_generate: bool
    review_after_generate: bool
    review_after_reflect: bool
    research_critique: str
    detailed: bool
    last_node: bool
    next_node: bool
    thread: str
    revision_number: int
    max_revisions: int
    human_review_before_generate: str
    human_review_after_generate: str
    human_review_after_reflect: str
    schemas: dict
    vdb_top_n_tables: List[Dict[str, Any]]
    kg_relevant_tables: List[str]
    kg_column_info: Dict[str, List[str]]
    kg_join_paths: List[Dict[str, List[str]]]
    kg_suggested_aggregations: List[str]
    kg_aggregations: List[str]
    objective: str
    tables_columns: str
    vdb_joins_where: str
    aggregations: str
    sorting_grouping: str
    ai_reflection: str
    content: List[str]
    full_history: List[AnyMessage]
    current_context: List[AnyMessage]
    result: str
    presigned_url: str


class Queries(BaseModel):
    queries: List[str]


class AgentWorkflow:
    def __init__(self, model, max_revisions=3, use_async=False):
        self.model = model
        self.max_revisions = max_revisions
        self.use_async = use_async
        self.vdb = MongoVectorDatabase()
        self.kg = KnowledgeGraph()
        self.kg.store_embeddings_in_neo4j()

    def update_message_collections(self, state: AgentState, new_message: AnyMessage, update_current_context: bool):
        state['full_history'].append(new_message)

        if update_current_context:
            state['current_context'].append(new_message)

        return state

    def define_objective_node(self, state):
        print('-'*30)
        print(f'define_objective_node')
        DEFINE_OBJECTIVE_PROMPT = """
        Important: Only perform the tasks explicitly stated in the instructions below. Do not generate any additional content or perform any other actions beyond what is explicitly requested.

        Your task is to define the objective of the Athena SQL query based on the user's requirements. 

        Define the objective of the query.
        """

        messages = [
            SystemMessage(content=DEFINE_OBJECTIVE_PROMPT),
            HumanMessage(content=state['query'])
        ]
        response = self.model.invoke(
            messages,
            temperature=0.2,     # Very low temperature for focused output
            max_tokens=250,       # Limit output length for a concise objective
            top_p=0.8,           # Slightly higher top_p for some flexibility in phrasing
            frequency_penalty=0.1, # Slight penalty to avoid repetitive language
            presence_penalty=0.1,  # Slight penalty to encourage conciseness
        )
        state['objective'] = response.content
        print(f"state['objective'] - {state['objective']}")
        print('-'*30)
        return state

    def should_review_objective(self, state):
        print('-'*30)
        print(f'should_review_objective')
        should_review = state.get('review_define_objective', False)
        print(f'should_review - {should_review}')
        print('-'*30)
        return "human_review_objective_node" if should_review else "get_database_schemas_node"

    def human_review_objective_node(self, state):
        print('-'*30)
        print(f'human_review_objective_node')
        human_review_objective = state.get('human_review_objective', '')
        additional_context = f" - the user reviewed the objective and decided to add this additional context to the query: {human_review_objective}"
        state['query'] = f"{state.get('query', '')} {additional_context}"
        print(f"Updated query - {state['query']}")
        print('-'*30)
        return state

    def get_database_schemas_node(self, state, database_name="aws_open_data_registry", collection_name="covid-19"):
        print('-'*30)
        print(f'get_database_schemas_node')
        if self.vdb.collection_exists(collection_name):
            print(f'collection_exists')
            return state
        state['schemas'] = get_database_schemas(state['database'])
        print('-'*30)
        return state

    def get_table_description_node(self, state, database_name="aws_open_data_registry", collection_name="covid-19"):
        print('-'*30)
        print(f'get_table_description_node')
        if self.vdb.collection_exists(collection_name):
            print(f'collection_exists')
            return state
        schemas = state.get('schemas', {})

        for table_name, schema in schemas.items():
            description_prompt = f"""
            Important: Only perform the tasks explicitly stated in the instructions below. Do not generate any additional content or perform any other actions beyond what is explicitly requested.

            You are an expert database analyst.
            Provide a description for the table "{table_name}" with the following columns: {schema['columns']}.
            The description should explain the purpose and content of the table.


            Important: Only perform the tasks explicitly stated in the instructions above. 
            Do not generate any additional content or perform any other actions beyond what is explicitly requested.
            """
            messages = [
                SystemMessage(content=description_prompt)
            ]

            response = self.model.invoke(
                messages,
                temperature=0.3,     # Low temperature for focused output
                max_tokens=250,      # Limit output length for conciseness
                top_p=0.7,           # Narrow down probability mass
                frequency_penalty=0, # No penalty for frequency
                presence_penalty=0,  # No penalty for presence
            )
            description = response.content.strip()
            schemas[table_name]['description'] = description
            # print(schemas[table_name]['description'])

        state['schemas'] = schemas
        print('-'*30)
        return state

    def create_vector_database_node(self, state):
        print('-'*30)
        print(f'create_vector_database_node')
        self.vdb.add_to_vector_db(state['schemas'])
        print('-'*30)
        return state

    def create_knowledge_graph_node(self, state):
        print('-'*30)
        print(f'create_knowledge_graph_node')
        if state['database'] != 'covid-19':
            self.kg.add_tables_and_joins()
        print('-'*30)
        return state

    def identify_tables_columns_node(self, state, n_results=5):
        print('-'*30)
        print(f'identify_tables_columns_node')
        IDENTIFY_TABLES_COLUMNS_PROMPT = """
        Important: Only perform the tasks explicitly stated in the instructions below. Do not generate any additional content or perform any other actions beyond what is explicitly requested.

        Your task is to identify the relevant tables needed for the Athena SQL query based on the defined {objective}.

        Given the top_n_result (listed below) from the query of the vector database, determine which table or tables are needed to answer the defined {objective}.

        Print only the table name(s) that match the objective and nothing else. 
        Output should be in the following format: table_name or table_name, table_name
        Do not include any additional text, punctuation, or formatting.

        vdb_top_n_tables:
        {vdb_top_n_tables}
        """

        state['vdb_top_n_tables'] = self.vdb.query_vector_db(state['objective'], n_results=n_results)
        state['kg_relevant_tables'] = self.kg.identify_relevant_tables(state['objective'], n_results=n_results)
        prompt = IDENTIFY_TABLES_COLUMNS_PROMPT.format(objective=state['objective'],
                                                       vdb_top_n_tables=state['vdb_top_n_tables'],
                                                       n_results=n_results
                                                       )
        
        messages = [
            SystemMessage(content=prompt)
        ]

        response = self.model.invoke(
                                    messages,
                                    temperature=0.1,  # Low temperature for focused and deterministic output
                                    max_tokens=100,   # Limit the output length
                                    top_p=0.6,        # Narrow down the probability mass for more focused results
                                    frequency_penalty=0,  # No penalty for frequency
                                    presence_penalty=0    # No penalty for presence
                                    )
        state['tables_columns'] = response.content
        print(f"state['tables_columns'] - {state['tables_columns']}")
        return state

    def outline_joins_where_conditions_node(self, state):
        print('-'*30)
        print(f'outline_joins_where_conditions_node')
        print(f"Joins for {state['tables_columns']}:")
        for source_table, related_table, join_column in state['vdb_joins_where']:
            print(f"{source_table} joins with {related_table} on column: {join_column}")
        print(f"state['vdb_joins_where'] - {state['vdb_joins_where']}")
        state['kg_join_paths'] = self.kg.find_join_paths(state['kg_relevant_tables']) if len(state['kg_relevant_tables']) > 1 else []
        #print(f"state['kg_join_paths'] - {state['kg_join_paths']}")
        print('-'*30)
        return state

    def specify_aggregations_node(self, state):
        print('-'*30)
        print(f'specify_aggregations_node')
        column_info = self.kg.get_column_info(state['kg_relevant_tables'])
        all_columns = [col for cols in column_info.values() for col in cols]
        state['kg_aggregations'] = self.kg.suggest_aggregations(state['objective'], all_columns)
        print(f"kg_aggregations - {state['kg_aggregations']}")
        print('-'*30)
        return state
    
    def should_review_before_generate(self, state):
        print('-'*30)
        print(f'should_review_before_generate')
        should_review = state.get('review_before_generate', False)
        print(f'should_review - {should_review}')
        print('-'*30)
        return "human_review_before_generate_node" if should_review else "generation_node"

    def human_review_before_generate_node(self, state):
        print('-'*30)
        print(f'human_review_before_generate_node')
        human_review_before_generate = state.get('human_review_before_generate', '')
        additional_context = f""
        state['human_review_before_generate'] = f"{state.get('human_review_before_generate', '')} {additional_context}"
        print(f"Updated human_review_before_generate - {state['human_review_before_generate']}")
        print('-'*30)
        return state

    def generation_node(self, state, n_results=5):
        print('-'*30)
        print(f'generation_node')

        ai_reflection_exists = state.get('ai_reflection') != ""
        if not ai_reflection_exists:
            print(f"ai_reflection_exists - {ai_reflection_exists}")
            WRITER_PROMPT = """
            Important: Only perform the tasks explicitly stated in the instructions below. Do not generate any additional content or perform any other actions beyond what is explicitly requested.

            You are an expert SQL query assistant tasked with writing high-quality SQL queries for Athena. 
            Your goal is to generate the best possible SQL query based on the defined objective.

            Provide only the SQL query, without any explanatory text.

            ------

            objective:
            {objective}

            Vector Database identified table(s):
            {vdb_top_n_tables}

            Knowledge Graph identified table(s):
            {kg_relevant_tables}

            Vector Database Possible Joins:
            {vdb_joins_where}

            Knowledge Graph Possible Joins:
            {kg_join_paths}

            Knowledge Graph Possible Aggregations:
            {kg_aggregations}
            """
            prompt = WRITER_PROMPT.format(objective=state.get('objective', ''),
                                          vdb_top_n_tables=state.get('vdb_top_n_tables', ''),
                                          kg_relevant_tables=state.get('kg_relevant_tables', ''),
                                          vdb_joins_where=state.get('vdb_joins_where', ''),
                                          kg_join_paths=state.get('kg_join_paths', ''),
                                          kg_aggregations=state.get('kg_aggregations', '')
                                          )
        else:
            print(f"ai_reflection_exists - {ai_reflection_exists}")
            WRITER_PROMPT = """
            Important: Only perform the tasks explicitly stated in the instructions below. Do not generate any additional content or perform any other actions beyond what is explicitly requested.

            You are an expert SQL query assistant tasked with writing high-quality SQL queries for Athena. Your goal is to generate the best possible SQL query based suggested improvements.

            Provide only the SQL query, without any explanatory text.

            improvements:
            {ai_refleciton}

            objective:
            {objective}

            Vector Database identified table(s):
            {vdb_top_n_tables}

            Knowledge Graph identified table(s):
            {kg_relevant_tables}

            Vector Database Possible Joins:
            {vdb_joins_where}

            Knowledge Graph Possible Joins:
            {kg_join_paths}

            Knowledge Graph Possible Aggregations:
            {kg_aggregations}
            """
            prompt = WRITER_PROMPT.format(objective=state.get('objective', ''),
                                          ai_refleciton=state.get('ai_refleciton', ''),
                                          vdb_top_n_tables=state.get('vdb_top_n_tables', ''),
                                          kg_relevant_tables=state.get('kg_relevant_tables', ''),
                                          vdb_joins_where=state.get('vdb_joins_where', ''),
                                          kg_join_paths=state.get('kg_join_paths', ''),
                                          kg_aggregations=state.get('kg_aggregations', '')
                                          )

        print('WRITER_PROMPT')
        print(prompt)

        messages = [
            SystemMessage(content=prompt),
        ]
        response = self.model.invoke(
            messages,
            temperature=0.1,     # Very low temperature for highly focused and deterministic output
            max_tokens=300,      # Allow for a longer response to accommodate the full SQL query
            top_p=0.95,          # High top_p for precise language in SQL context
            frequency_penalty=0, # No penalty for repeating SQL keywords
            presence_penalty=0,  # No penalty for presence to allow necessary repetition
            stop=[";"]   # Stop at end of query or double newline to prevent additional content
        )
        state['result'] = strip_markdown_code_block(response.content)
        print(f"state['result'] - {state['result']}")
        print('-'*30)
        return state

    def should_review_after_generate(self, state):
        print('-'*30)
        print(f'should_review_after_generate')
        should_review = state.get('review_after_generate', False)
        print(f'should_review - {should_review}')
        print('-'*30)
        return "human_review_after_generate_node" if should_review else "execute_athena_query_node"

    def human_review_after_generate_node(self, state):
        print('-'*30)
        print(f'human_review_after_generate_node')
        additional_context = f""
        state['human_review_after_generate_node'] = f"{state.get('human_review_after_generate_node', '')} {additional_context}"
        print(f"Updated human_review_after_generate_node - {state['human_review_after_generate_node']}")
        print('-'*30)
        return state

    def execute_athena_query_node(self, state):
        print('-'*30)
        print(f'execute_athena_query_node')
        state['presigned_url'] = execute_athena_query_function(state['result'], state['database'])
        print(f"state['presigned_url'] - {state['presigned_url']}")
        print('-'*30)
        return state

    def check_query_success(self, state):
        print('-'*30)
        print(f'check_query_success')
        pattern = re.compile(r"https:\/\/.*\.s3\.amazonaws\.com\/.*")
        presigned_url = state.get('presigned_url', '')

        if pattern.match(presigned_url):
            print(f'pattern.match(presigned_url)')
            return END
        else:
            state['revision_number'] = int(state.get('revision_number', 0)) + 1
            print(f"revision_number - {state['revision_number']}")
            if state["revision_number"] > state["max_revisions"]:
                return END  # Or handle as a different failure state if desired
            else:
                return "reflection_node"

    def reflection_node(self, state):
        print('-'*30)
        print(f'reflection_node')

        REFLECTION_PROMPT = """
        You are an experienced data analyst tasked with reviewing an Athena SQL query submission. 
        Your goal is to provide comprehensive critique and recommendations to enhance fix the SQL query.
        Follow these steps:

        1. Thoroughly read the user's SQL query submission.
        Athena SQL query submission:
        {result}

        2. Thoroughly read the error message.
        Error message:
        {presigned_url}

        3. Given the error message, provide a detailed critique of areas for improvement.
        4. Ensure your feedback is actionable and constructive, enabling the user to improve their SQL query effectively.
        """

        objective = state.get('objective', '')
        result = state.get('result', '')
        presigned_url = state.get('presigned_url', '')

        prompt = REFLECTION_PROMPT.format(objective=objective, result=result,presigned_url=presigned_url)

        messages = [
            SystemMessage(content=prompt),
        ]
        response = self.model.invoke(
            messages,
            temperature=0.2,     # Low temperature for focused and structured output
            max_tokens=500,      # Allow for a longer response to provide comprehensive feedback
            top_p=0.9,           # High top_p for precise language in SQL context
            frequency_penalty=0, # No penalty for repeating SQL keywords
            presence_penalty=0,  # No penalty for presence to allow necessary repetition
        )
        state['ai_reflection'] = response.content
        print(f"ai_reflection - {state['ai_reflection']}")
        print('-'*30)
        return state

    def should_review_after_reflect(self, state):
        print('-'*30)
        print(f'should_review_after_reflect')
        should_review = state.get('review_after_reflect', False)
        print(f'should_review - {should_review}')
        print('-'*30)
        return "human_review_after_reflect_node" if should_review else "generation_node"

    def human_review_after_reflect_node(self, state):
        print('-'*30)
        print(f'human_review_after_reflect_node')
        state['human_review_after_reflect_node'] = f"{state.get('human_review_after_reflect_node', '')} {additional_context}"
        print(f"Updated human_review_after_reflect_node - {state['human_review_after_reflect_node']}")
        print('-'*30)
        return state

    def create_and_run_graph(self, state, thread, memory):
        print('-'*30)
        print(f'create_and_run_graph')

        builder = StateGraph(AgentState)

        # Adding nodes including human-in-the-loop steps
        nodes_to_add = [
            ("define_objective_node", self.define_objective_node),
            ("human_review_objective_node", self.human_review_objective_node),
            ("get_database_schemas_node", self.get_database_schemas_node),
            ("table_description_node", self.get_table_description_node),
            ("create_vector_database_node", self.create_vector_database_node),
            ("create_knowledge_graph_node", self.create_knowledge_graph_node),
            ("identify_tables_columns_node", self.identify_tables_columns_node),
            ("outline_joins_where_conditions_node", self.outline_joins_where_conditions_node),
            ("specify_aggregations_node", self.specify_aggregations_node),
            ("human_review_before_generate_node", self.human_review_before_generate_node),
            ("generation_node", self.generation_node),
            ("human_review_after_generate_node", self.human_review_after_generate_node),
            ("execute_athena_query_node", self.execute_athena_query_node),
            ("reflection_node", self.reflection_node),
            ("human_review_after_reflect_node", self.human_review_after_reflect_node),
        ]

        state_keys = set(state.keys())
        for node_name, node_method in nodes_to_add:
            return_annotation = node_method.__annotations__.get('return', {})
            if isinstance(return_annotation, dict):
                for key in return_annotation.keys():
                    if key in state_keys:
                        print(f"Warning: Key '{key}' from node '{node_name}' conflicts with existing state key")
                    else:
                        state_keys.add(key)

        for node_name, node_method in nodes_to_add:
            print(f"Attempting to add node: {node_name}")
            if not hasattr(self, node_method.__name__):
                print(f"Error: Method {node_method.__name__} not found in AgentWorkflow")
                continue
            try:
                builder.add_node(node_name, node_method)
                print(f"Successfully added node: {node_name}")
            except Exception as e:
                print(f"Error adding node {node_name}: {str(e)}")
        

        # Set entry point and add edges
        builder.set_entry_point("define_objective_node")
        builder.add_conditional_edges(
            "define_objective_node",
            self.should_review_objective,
            {"human_review_objective_node": "human_review_objective_node", "get_database_schemas_node": "get_database_schemas_node"}
        )

        builder.add_edge("human_review_objective_node", "get_database_schemas_node")
        builder.add_edge("get_database_schemas_node", "table_description_node")
        builder.add_edge("table_description_node", "create_vector_database_node")
        builder.add_edge("create_vector_database_node", "create_knowledge_graph_node")
        builder.add_edge("create_knowledge_graph_node", "identify_tables_columns_node")
        builder.add_edge("identify_tables_columns_node", "outline_joins_where_conditions_node")
        builder.add_edge("outline_joins_where_conditions_node", "specify_aggregations_node")
        builder.add_conditional_edges(
            "specify_aggregations_node",
            self.should_review_before_generate,
            {"human_review_before_generate_node": "human_review_before_generate_node", "generation_node": "generation_node"}
        )
        builder.add_edge("human_review_before_generate_node", "generation_node")

        builder.add_conditional_edges(
            "generation_node",
            self.should_review_after_generate,
            {"human_review_after_generate_node": "human_review_after_generate_node", "execute_athena_query_node": "execute_athena_query_node"}
        )
        builder.add_edge("human_review_after_generate_node", "execute_athena_query_node")

        builder.add_conditional_edges(
            "execute_athena_query_node",
            self.check_query_success,
            {END: END, "reflection_node": "reflection_node"}
        )

        builder.add_conditional_edges(
            "reflection_node",
            self.should_review_after_reflect,
            {"human_review_after_reflect_node": "human_review_after_reflect_node", "generation_node": "generation_node"}
        )
        builder.add_edge("human_review_after_reflect_node", "generation_node")

        # Compile the state graph
        print("Compiling the state graph...")
        graph = builder.compile(checkpointer=memory)

        # Stream the graph and print the outputs
        print("Streaming the graph...")
        for s in graph.stream(state, thread):
            #print(s)
            final_state = s

        self.kg.close()
        print('-'*30)
        return final_state


def strip_markdown_code_block(query):
    # Remove the ```sql and ``` lines
    lines = query.split('\n')
    stripped_lines = [line for line in lines if not line.strip().startswith('```')]
    return '\n'.join(stripped_lines)

def writer(*args, use_async=False, **kwargs):
    print('-'*30)
    print('writer')
    query = args[0]
    database = args[1]
    review_define_objective = args[2]
    review_before_generate = args[3]
    review_after_generate = args[4]
    review_after_reflect = args[5]
    research_critique = args[6]
    detailed = args[7]
    last_node = args[8]
    next_node = args[9]
    thread = args[10]
    revision_number = int(args[11])
    print(f'query - {query}')

    state = {
        'query': query,
        'database': database,
        'review_define_objective': review_define_objective,
        'review_before_generate': review_before_generate,
        'review_after_generate': review_after_generate,
        'review_after_reflect': review_after_reflect,
        'research_critique': research_critique,
        'detailed': detailed,
        'last_node': last_node,
        'next_node': next_node,
        'thread': thread,
        'revision_number': revision_number,
        'max_revisions': 3,
        'human_review_before_generate': "",
        'human_review_after_generate': "",
        'human_review_after_reflect': "",
        'schemas': {},
        'vdb_top_n_tables': [],
        'objective': "",
        'tables_columns': "",
        'vdb_joins_where': "",
        'aggregations': "",
        'sorting_grouping': "",
        'ai_reflection': "",
        'content': [],
        'full_history': [HumanMessage(content=query)],
        'current_context': [HumanMessage(content=query)],
        'result': "",
        'presigned_url': ""
    }

    if use_async:
        memory = AsyncSqliteSaver.from_conn_string(":memory:")
    else:
        memory = SqliteSaver.from_conn_string(":memory:")

    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    agent_workflow = AgentWorkflow(model=model)

    final_state = agent_workflow.create_and_run_graph(state, thread, memory)
    print('-'*30)
    return (
        final_state['execute_athena_query_node']['query'],
        final_state['execute_athena_query_node']['database'],
        review_define_objective,
        review_before_generate,
        review_after_generate,
        review_after_reflect,
        research_critique,
        detailed,
        last_node,
        next_node,
        thread,
        final_state['execute_athena_query_node']['revision_number'],
        "",
        final_state['execute_athena_query_node']['result'],
        final_state['execute_athena_query_node']['presigned_url']
    )
