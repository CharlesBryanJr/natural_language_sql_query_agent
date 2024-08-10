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

import sys
import os
import json
import copy

# Add the project root directory and server_python directory to the sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
server_python_path = os.path.join(project_root, 'server_python')
agents_path = os.path.join(server_python_path, 'agents')
api_path = os.path.join(server_python_path, 'api')

sys.path.append(project_root)
sys.path.append(server_python_path)
sys.path.append(agents_path)
sys.path.append(api_path)

from flask import request, jsonify
from server_python.agents.athena_agent import writer
from api.athena_operations import execute_athena_query_function

def ask_question():
    try:
        print('-'*30)
        print('ask_question')
        data = request.get_json()

        fallback_data = {
            "query": "write a SQL query calculates the total number of COVID-19 tests conducted in each state and then list these states in descending order based on the volume of tests, starting with the state that has conducted the most tests.",
            "database": "covid-19",
            "review_define_objective": False,
            "review_before_generate": False,
            "review_after_generate": False,
            "review_after_reflect": False,
            "research_critique": False,
            "Detailed": False,
            "lastNode": None,
            "nextNode": None,
            "thread": {"configurable": {"thread_id": "1"}},
            "draftRev": 0,
            "count": 0,
            "writer_result": None,
            "presigned_url": None
        }

        query = need_fallback_data(data, fallback_data, 'query')
        database = need_fallback_data(data, fallback_data, 'database')
        review_define_objective = need_fallback_data(data, fallback_data, 'review_define_objective')
        review_before_generate = need_fallback_data(data, fallback_data, 'review_before_generate')
        review_after_generate = need_fallback_data(data, fallback_data, 'review_after_generate')
        review_after_reflect = need_fallback_data(data, fallback_data, 'review_after_reflect')
        research_critique = need_fallback_data(data, fallback_data, 'research_critique')
        Detailed = need_fallback_data(data, fallback_data, 'Detailed')
        lastNode = need_fallback_data(data, fallback_data, 'lastNode')
        nextNode = need_fallback_data(data,fallback_data, 'nextNode')
        thread = need_fallback_data(data, fallback_data, 'thread')
        draftRev = need_fallback_data(data, fallback_data, 'draftRev')
        count = need_fallback_data(data, fallback_data, 'count')
        writer_result = need_fallback_data(data, fallback_data, 'writer_result')
        presigned_url = need_fallback_data(data, fallback_data, 'presigned_url')


        args = (query, database, review_define_objective, review_before_generate, review_after_generate, review_after_reflect, research_critique, Detailed, lastNode, nextNode, thread, draftRev, count, writer_result, presigned_url)

        # writer_result = writer(query)
        # writer_result, presigned_url = writer(query, database)
        # writer_result = "SELECT state, SUM(totaltestresults) AS total_tests_conducted FROM covid_testing_states_daily GROUP BY state ORDER BY total_tests_conducted DESC;"
        (result_query, result_database, result_review_define_objective, result_review_before_generate, 
                result_review_after_generate, result_review_after_reflect, result_research_critique, 
                result_Detailed, result_lastNode, result_nextNode, result_thread, result_draftRev, 
                result_count, result_writer_result, result_presigned_url) = writer(*args)

        # presigned_url = execute_athena_query_function(writer_result, database)
        # presigned_url = "https://covid19-data-lake-results.s3.amazonaws.com/LLM/260cd42d-b2d5-42b3-8ef8-3129c369f61d.csv?response-expires=Thu%2C%2001%20Jan%201970%2000%3A06%3A00%20GMT&AWSAccessKeyId=AKIAQ3EGUGAZG4LXU3ES&Signature=f%2FU%2F13rGmVKQB6PI2pP6o34SpDYqvg%3D&Expires=1720111662"

        destructed = {
            "query": result_query,
            "database": result_database,
            "review_define_objective": result_review_define_objective,
            "review_before_generate": result_review_before_generate,
            "review_after_generate": result_review_after_generate,
            "review_after_reflect": result_review_after_reflect,
            "research_critique": result_research_critique,
            "Detailed": result_Detailed,
            "lastNode": result_lastNode,
            "nextNode": result_nextNode,
            "thread": result_thread,
            "draftRev": result_draftRev,
            "count": result_count,
            "writer_result": result_writer_result,
            "presigned_url": result_presigned_url
        }

        print('-'*30)
        return jsonify(destructed)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500


def need_fallback_data(data, fallback_data, key):
    value = data.get(key)
    return value if value is not None else fallback_data.get(key)


'''
        print(' ')
        print('Post Writer')
        print(' ')

        print(f"query: {query}")
        print(f"database: {database}")
        print(f"review_define_objective: {review_define_objective}")
        print(f"review_before_generate: {review_before_generate}")
        print(f"review_after_generate: {review_after_generate}")
        print(f"review_after_reflect: {review_after_reflect}")
        print(f"research_critique: {research_critique}")
        print(f"Detailed: {Detailed}")
        print(f"lastNode: {lastNode}")
        print(f"nextNode: {nextNode}")
        print(f"thread: {thread}")
        print(f"draftRev: {draftRev}")
        print(f"count: {count}")
        print(f"writer_result: {writer_result}")
        print(f"presigned_url: {presigned_url}")

'''