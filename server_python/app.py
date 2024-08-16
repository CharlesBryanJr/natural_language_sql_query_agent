import os
import sys
from flask import Flask, request, jsonify
from dotenv import load_dotenv, find_dotenv
from flask_cors import CORS
load_dotenv(find_dotenv())

try:
    # Find the 'routes' directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    routes_dir = None

    for root, dirs, files in os.walk(parent_dir):
        if 'routes' in dirs:
            routes_dir = os.path.join(root, 'routes')
            break

    if routes_dir:
        sys.path.append(os.path.dirname(routes_dir))
    else:
        print("'routes' directory not found")
        sys.exit(1)

    # Now try to import agent_bp
    from routes.agent_routes import agent_bp

    # Load environment variables
    load_dotenv(find_dotenv())

    # Initialize Flask app
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Register blueprints
    app.register_blueprint(agent_bp, url_prefix='/api')

    # Add a root route for health checks
    @app.route('/')
    def home():
        try:
            openai_api_key = os.getenv('openai_api_key')
            OPENAI_API_KEY = os.getenv('openai_api_key')
            if openai_api_key:
                return f"App is running on Vercel! OpenAI API Key: {openai_api_key}"
            else:
                raise ValueError("OPENAI_API_KEY is not set")
        except Exception as e:
            app.logger.error(f"Error in home route: {str(e)} - Environment variables: {os.environ}")
            return jsonify({"error": "An internal error occurred"}), 500


    # Add a route to help diagnose the 403 error
    @app.route('/debug', methods=['GET', 'POST'])
    def debug():
        try:
            headers = dict(request.headers)
            env_vars = {key: os.getenv(key) for key in os.environ.keys()}
            return jsonify({"headers": headers, "env_vars": env_vars, "message": "Debugging info"}), 200
        except Exception as e:
            app.logger.error(f"Error in debug route: {str(e)}")
            return jsonify({"error": "An error occurred while debugging"}), 500


    # This is important for Vercel
    wsgi_app = app.wsgi_app

    # Local development
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5001, debug=True)

except Exception as e:
    print(f"An error occurred during app initialization: {str(e)}")
    sys.exit(1)