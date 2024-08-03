import os
import sys
import json
import chromadb
import openai
from get_table_schema import get_database_schemas
from dotenv import load_dotenv, find_dotenv

load_dotenv('/Users/charlesbryan/Desktop/CharlesTMS/.env')

class VectorDatabase:
    def __init__(self, collection_name="my_collection", openai_api_key=None):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(collection_name)
        self.collection_name = collection_name
        self.openai_api_key = openai_api_key or os.getenv("OPENAI_API_KEY")

    def get_embedding(self, text):
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
        for key, value in data_dict.items():
            document = json.dumps(value)
            id = key
            embedding = self.get_embedding(document)
            # print(f"Adding to vector DB - ID: {id}, Document: {document}, Embedding: {embedding}")

            self.collection.add(
                embeddings=[embedding],
                documents=[document],
                ids=[id]
            )

    def query_vector_db(self, query, n_results=3):
        query_embedding = self.get_embedding(query)
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        return results

    def to_dict(self):
        """Custom serialization method"""
        return {
            'collection_name': self.collection_name,
            'openai_api_key': self.openai_api_key
        }

    @classmethod
    def from_dict(cls, data):
        """Custom deserialization method"""
        instance = cls(
            collection_name=data['collection_name'],
            openai_api_key=data['openai_api_key']
        )
        # Reconnect to the collection
        instance.collection = instance.client.get_collection(data['collection_name'])
        return instance

'''
if __name__ == "__main__":
    print('-'*30)
    database_name = "covid-19"
    schemas = get_database_schemas(database_name)

    vdb = VectorDatabase(openai_api_key=openai.api_key)
    vdb.add_to_vector_db(schemas)

    query = "write a SQL query calculates the total number of COVID-19 tests conducted in each state and then list these states in descending order based on the volume of tests, starting with the state that has conducted the most tests."
    print('query - ', query)
    results = vdb.query_vector_db(query)

    print("Query Results:")
    for i, (id, document, metadata, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0],
        results['metadatas'][0], results['distances'][0]
    )):
        print(f"\nResult {i+1}:")
        print(f"ID: {id}")
        print(f"Document: {json.loads(document)}")
        print(f"Metadata: {metadata}")
        print(f"Distance: {distance}")
'''