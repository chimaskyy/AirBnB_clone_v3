#!/usr/bin/python3
"""script returns the status of our API"""
import os

from flask import Flask, jsonify
from flask_cors import CORS

from api.v1.views import app_views
from models import storage

app = Flask(__name__)

app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def tear_down(exception):
    """handles the teardown context"""
    storage.close()


@app.errorhandler(404)
def not_found_handler(exception):
    """
    handler for 404 errors that returns a JSON-formatted 404 status code
    response
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    HOST = os.getenv("HBNB_API_HOST", "0.0.0.0")
    PORT = os.getenv("HBNB_API_PORT", "5000")

    app.run(host=HOST, port=PORT, threaded=True)
