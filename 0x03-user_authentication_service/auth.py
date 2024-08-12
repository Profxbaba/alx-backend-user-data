#!/usr/bin/env python3
"""
Auth class to handle user authentication and registration.
"""

from db import DB
from models.user import User
import bcrypt

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialize Auth with a DB instance."""
        self._db = DB()

    def _hash_password(self, password: str) -> str:
        """Hash a password string using bcrypt.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with the given email and password.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Raises:
            ValueError: If a user with the given email already exists.

        Returns:
            User: The newly created User object.
        """
        if self._db.get_user_by_email(email):
            raise ValueError(f"User {email} already exists")
        
        hashed_password = self._hash_password(password)
        
        user = self._db.add_user(email, hashed_password)
        
        return user
