import os
from flask import Flask, request, jsonify
from routes.agent_routes import agent_bp
from dotenv import load_dotenv, find_dotenv
from flask_cors import CORS

# Load environment variables
load_dotenv(find_dotenv())

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Register blueprints
app.register_blueprint(agent_bp, url_prefix='/api')

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