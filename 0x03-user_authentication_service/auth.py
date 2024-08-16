#!/usr/bin/env python3
"""
This module provides authentication methods, including password hashing
and user registration.
"""

import bcrypt
from db import DB
from user import User  # Assuming a User class exists in user.py
from sqlalchemy.exc import NoResultFound  # Import the exception


def _hash_password(password: str) -> bytes:
    """
    Hashes a password string using bcrypt & returns hashed password as bytes.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted and hashed password.
    """
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialize the Auth class with a DB instance."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user with the given email and password.

        Args:
            email (str): The email address of the user.
            password (str): The password for the user.

        Returns:
            User: The created User object.

        Raises:
            ValueError: If a user with the given email already exists.
        """
        try:
            # Check if the user already exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # If no user is found, proceed with user creation
            pass

        # Hash the password
        hashed_password = _hash_password(password)

        # Create the new user
        new_user = User(email=email, hashed_password=hashed_password)

        # Save the new user to the database
        self._db.add_user(email=email, hashed_password=hashed_password)

        return new_user
