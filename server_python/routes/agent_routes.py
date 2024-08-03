import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from flask import Blueprint
from server_python.controllers.agent_controller import ask_question

agent_bp = Blueprint('agent_bp', __name__)

agent_bp.route('/ask', methods=['POST'])(ask_question)