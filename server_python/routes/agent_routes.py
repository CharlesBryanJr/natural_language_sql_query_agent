import sys
import os
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from controllers.agent_controller import ask_question

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

# Initialize the blueprint
agent_bp = Blueprint('agent_bp', __name__)
CORS(agent_bp)  # Enable CORS for this blueprint

agent_bp.route('/ask', methods=['POST'])(ask_question)
