#!/usr/bin/env python3
"""
Flask application module for handling user creation.
"""

from flask import Flask, request, jsonify, abort
from auth import Auth

app = Flask(__name__)
auth = Auth()


@app.route('/users', methods=['POST'])
def register_user() -> str:
    """
    Handles POST requests to /users for user registration.

    Checks the provided email and password, registers the user if valid,
    and returns a JSON payload with the success message or error message.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        abort(400, description="Email and password are required")

    try:
        auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError as e:
        return jsonify({"message": str(e)}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
