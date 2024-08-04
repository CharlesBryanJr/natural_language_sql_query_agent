import sys
import os
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from server_python.controllers.agent_controller import ask_question

# Initialize the blueprint
agent_bp = Blueprint('agent_bp', __name__)
CORS(agent_bp)  # Enable CORS for this blueprint

# Route definition
@agent_bp.route('/ask', methods=['POST'])
def ask():
    if request.method == 'POST':
        try:
            data = request.json
            response = ask_question()
            return jsonify({"message": "Request received", "data": data}), 200  # Temporary response
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"message": "Method not allowed"}), 405