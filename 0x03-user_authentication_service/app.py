#!/usr/bin/env python3
"""
A basic Flask application that returns a JSON payload.
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home() -> jsonify:
    """
    Handle GET requests to the root URL and return a JSON response.

    Returns:
        jsonify: A JSON response with a welcome message.
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
