import os
from flask import Flask
from routes.agent_routes import agent_bp
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Initialize Flask app
app = Flask(__name__)

# Register blueprints
app.register_blueprint(agent_bp, url_prefix='/api')

# Add a root route for health checks
@app.route('/')
def home():
    return "Flask app is running on Vercel!"

# This is important for Vercel
wsgi_app = app.wsgi_app

# local development
if __name__ == '__main__':
    app.run(debug=True)