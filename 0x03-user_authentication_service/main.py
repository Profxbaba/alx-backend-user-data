#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'bob@bob.com'  # Ensure this email is unique
password = 'MyPwdOfBob'
auth = Auth()

# Register a new user
try:
    auth.register_user(email, password)
except ValueError as e:
    print(f"Error: {e}")

# Create a session for the registered user
print(auth.create_session(email))

# Attempt to create a session for an unknown email
print(auth.create_session("unknown@example.com"))
