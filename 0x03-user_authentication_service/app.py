#!/usr/bin/env python3
"""
Flask application for user registration.
"""

from flask import Flask, request, jsonify
from auth import Auth

# Initialize Flask app and Auth instance
app = Flask(__name__)
AUTH = Auth()


@app.route('/users', methods=['POST'])
def register_user():
    """
    Handles user registration via POST request to /users.
    Expects 'email' and 'password' fields in form data.

    Returns:
        JSON: A response with the email and a message if the user is created.
        JSON: A response with a message and status 400 if email isregistered.
        """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({"message": "email and password are required"}), 400

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError as err:
        return jsonify({"message": str(err)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
