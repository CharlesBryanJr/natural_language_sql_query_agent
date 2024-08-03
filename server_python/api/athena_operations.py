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

import time
import traceback
import boto3

athena = boto3.client('athena', region_name='us-west-2')
s3 = boto3.client('s3', region_name='us-west-2')

def start_query_execution(query,
                          database=None,
                          workgroup='primary',
                          s3_output='s3://covid19-data-lake-results/LLM',
                          catalog=None,
                          client_request_token=None,
                          encryption_config=None,
                          expected_bucket_owner=None,
                          acl_config=None,
                          execution_parameters=None,
                          result_reuse_config=None):

    query_execution_context = {}
    if database:
        query_execution_context['Database'] = database
    if catalog:
        query_execution_context['Catalog'] = catalog

    result_configuration = {'OutputLocation': s3_output}
    if encryption_config:
        result_configuration['EncryptionConfiguration'] = encryption_config
    if expected_bucket_owner:
        result_configuration['ExpectedBucketOwner'] = expected_bucket_owner
    if acl_config:
        result_configuration['AclConfiguration'] = acl_config

    params = {
        'QueryString': query,
        'WorkGroup': workgroup,
        'ResultConfiguration': result_configuration
    }
    if client_request_token:
        params['ClientRequestToken'] = client_request_token
    if query_execution_context:
        params['QueryExecutionContext'] = query_execution_context
    if execution_parameters:
        params['ExecutionParameters'] = execution_parameters
    if result_reuse_config:
        params['ResultReuseConfiguration'] = result_reuse_config

    response = athena.start_query_execution(**params)
    return response['QueryExecutionId']

def check_query_status(query_execution_id):
    while True:
        response = athena.get_query_execution(QueryExecutionId=query_execution_id)
        status = response['QueryExecution']['Status']['State']
        if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            error_message = response['QueryExecution']['Status'].get('StateChangeReason', None)
            if status == 'FAILED':
                print(f"Query failed. Error: {error_message}")
            return status, error_message
        time.sleep(2)

def generate_presigned_url(bucket, key):
    try:
        s3_params = {
            'Bucket': bucket,
            'Key': key,
            'ResponseExpires': 360
        }
        url = s3.generate_presigned_url('get_object', Params=s3_params)
        return url
    except boto3.exceptions.S3UploadFailedError as e:
        # Handle specific S3 upload failed error
        error_message = f"S3UploadFailedError: {str(e)}. Bucket: {bucket}, Key: {key}"
        print(error_message)
        return error_message
    except Exception as e:
        # Capture and return a detailed error message
        error_message = f"An unexpected error occurred: {str(e)}. Bucket: {bucket}, Key: {key}. Traceback: {traceback.format_exc()}"
        print(error_message)
        return error_message

def execute_athena_query_function(query, database):
    try:
        query_execution_id = start_query_execution(query, database)
        status, error_message = check_query_status(query_execution_id)
        if status != 'SUCCEEDED':
            return f"Query execution failed with status: {status}. Error: {error_message}"

        query_results = athena.get_query_execution(QueryExecutionId=query_execution_id)
        s3_output_location = query_results['QueryExecution']['ResultConfiguration']['OutputLocation']
        s3_bucket = s3_output_location.split('/')[2]
        s3_key = '/'.join(s3_output_location.split('/')[3:])

        presigned_url = generate_presigned_url(s3_bucket, s3_key)
        return presigned_url
    except Exception as e:
        error_message = f"An unexpected error occurred during query execution: {str(e)}. Traceback: {traceback.format_exc()}"
        print(error_message)
        return error_message
