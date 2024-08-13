#!/usr/bin/env python3
"""
Auth module for handling user authentication.
"""

from werkzeug.security import generate_password_hash
from db import DB
from typing import Optional


class Auth:
    """
    Auth class for managing user authentication and session management.
    """
    def __init__(self):
        """
        Initializes the Auth instance with a DB instance.
        """
        self.db = DB()

    def register_user(self, email: str, password: str) -> None:
        """
        Registers a new user with the given email and password.

        If the user already exists, raises a ValueError with a message

        Args:
            email (str): The user's email address.
            password (str): The user's password.

        Raises:
            ValueError: If a user with the given email already exists.
        """
        if self.db.get_user_by_email(email):
            raise ValueError(f"User {email} already exists")

        hashed_password = generate_password_hash(password)
        self.db.add_user(email, hashed_password)
