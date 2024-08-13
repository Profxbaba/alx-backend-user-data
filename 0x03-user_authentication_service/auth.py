#!/usr/bin/env python3
"""
Module for user authentication.
"""

import uuid
from db import DB
import bcrypt


class Auth:
    """
    Class to handle authentication.
    """
    def __init__(self) -> None:
        """
        Initialize the Auth class.
        """
        self.db = DB()

    def register_user(self, email: str, password: str) -> None:
        """
        Register a user with an email and a hashed password.

        Args:
            email (str): The user's email.
            password (str): The user's password.
        """
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login with email and password.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            bool: True if the email exists and the password matches,
            """
        user = self.db.get_user_by_email(email)
        if user is None:
            return False
        hashed_password = user.password
        return bcrypt.checkpw(password.encode(), hashed_password)

    def _generate_uuid(self) -> str:
        """
        Generate a new UUID and return its string representation.

        Returns:
            str: A string representation of a new UUID.
        """
        return str(uuid.uuid4())
