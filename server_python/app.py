import os
import sys
from flask import Flask, request, jsonify
from dotenv import load_dotenv, find_dotenv
from flask_cors import CORS

# Ensure the project root is in the path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

try:
    from server_python.routes.agent_routes import agent_bp
    print("Successfully imported agent_bp from routes.agent_routes")
except ImportError as e:
    print("Failed to import agent_bp from routes.agent_routes:", str(e))

# Load environment variables
load_dotenv(find_dotenv())

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Register blueprints
if 'agent_bp' in globals():
    app.register_blueprint(agent_bp, url_prefix='/api')
else:
    print("agent_bp is not defined")

# Add a root route for health checks
@app.route('/')
def home():
    return "Flask app is running on EC2!"

# Add a route to help diagnose the 403 error
@app.route('/debug', methods=['GET', 'POST'])
def debug():
    headers = dict(request.headers)
    return jsonify({"headers": headers, "message": "Debugging info"}), 200

# This is important for Vercel
wsgi_app = app.wsgi_app

# Local development
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)