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
import boto3

# Function to retrieve the list of tables from the specified database
def get_table_names(database_name):
    client = boto3.client('glue')
    response = client.get_tables(DatabaseName=database_name)
    table_names = [table['Name'] for table in response['TableList']]
    return table_names

# Function to retrieve schema for a single table
def get_table_schema(database_name, table_name):
    client = boto3.client('glue')

    response = client.get_table(DatabaseName=database_name, Name=table_name)
    table = response['Table']

    schema = {}
    schema['TableName'] = table['Name']
    schema['Columns'] = [col['Name'] for col in table['StorageDescriptor']['Columns']]

    return schema

# Function to retrieve schemas for all tables in the database
def get_database_schemas(database_name):
    table_names = get_table_names(database_name)
    schemas = {}
    for table_name in table_names:
        schema = get_table_schema(database_name, table_name)
        schemas[schema['TableName']] = {
            'columns': schema['Columns'],
            'description': None
        }
    return schemas

'''
if __name__ == "__main__":
    # Specify the database name
    database_name = 'covid-19'

    # Retrieve the list of tables
    table_names = get_table_names(database_name)

    # Print the results
    print("\nSelected Database and Tables -")
    print(f"Database: {database_name}")
    print(f"Tables: {table_names}")

    # Retrieve schemas for the tables
    schemas = get_database_schemas(database_name)

    # Print the schemas
    print("\nSchemas -")
    for table, columns in schemas.items():
        print(f"Table: {table}, Columns: {columns}")
'''