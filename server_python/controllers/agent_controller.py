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

        # Destructure the JSON data into individual variables
        query = data.get('query')
        database = data.get('database')
        review_define_objective = data.get('review_define_objective')
        review_before_generate = data.get('review_before_generate')
        review_after_generate = data.get('review_after_generate')
        review_after_reflect = data.get('review_after_reflect')
        research_critique = data.get('research_critique')
        Detailed = data.get('Detailed')
        lastNode = data.get('lastNode')
        nextNode = data.get('nextNode')
        thread = data.get('thread')
        draftRev = data.get('draftRev')
        count = data.get('count')
        writer_result = data.get('writer_result')
        presigned_url = data.get('presigned_url')


        args = (query, database, review_define_objective, review_before_generate, review_after_generate, review_after_reflect, research_critique, Detailed, lastNode, nextNode, thread, draftRev, count, writer_result, presigned_url)

        # writer_result = writer(query)
        # writer_result, presigned_url = writer(query, database)
        # writer_result = "SELECT state, SUM(totaltestresults) AS total_tests_conducted FROM covid_testing_states_daily GROUP BY state ORDER BY total_tests_conducted DESC;"
        (query, database, review_define_objective, review_before_generate, review_after_generate, review_after_reflect, research_critique, Detailed, lastNode, nextNode, thread, draftRev, count, writer_result, presigned_url) = writer(*args)

        # presigned_url = execute_athena_query_function(writer_result, database)
        # presigned_url = "https://covid19-data-lake-results.s3.amazonaws.com/LLM/260cd42d-b2d5-42b3-8ef8-3129c369f61d.csv?response-expires=Thu%2C%2001%20Jan%201970%2000%3A06%3A00%20GMT&AWSAccessKeyId=AKIAQ3EGUGAZG4LXU3ES&Signature=f%2FU%2F13rGmVKQB6PI2pP6o34SpDYqvg%3D&Expires=1720111662"

        result = {
            "query": query,
            "database": database,
            "review_define_objective": review_define_objective,
            "review_before_generate": review_before_generate,
            "review_after_generate": review_after_generate,
            "review_after_reflect": review_after_reflect,
            "research_critique": research_critique,
            "Detailed": Detailed,
            "lastNode": lastNode,
            "nextNode": nextNode,
            "thread": thread,
            "draftRev": draftRev,
            "count": count,
            "writer_result": writer_result,
            "presigned_url": presigned_url
        }
        print('-'*30)
        return jsonify(result)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500


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