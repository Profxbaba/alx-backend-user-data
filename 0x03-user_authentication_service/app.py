#!/usr/bin/env python3
"""
Flask application to handle user registration.
"""

from flask import Flask, request, jsonify
from auth import Auth

# Instantiate the Auth class
AUTH = Auth()

app = Flask(__name__)


@app.route('/users', methods=['POST'])
def users() -> str:
    """
    Handles user registration. Expects 'email' and 'password' in form data.

    Returns:
        str: A JSON response indicating whether the user was created
             or already exists.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return (
            jsonify({"message": "email and password required"}), 400
        )

    try:
        user = AUTH.register_user(email, password)
        return (
            jsonify({"email": user.email, "message": "user created"}), 201
        )
    except ValueError as e:
        return jsonify({"message": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
