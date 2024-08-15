#!/usr/bin/env python3
"""
Auth module for handling user authentication.
"""
from typing import Optional
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


class Auth:
    """
    Auth class to manage user authentication.
    """

    def __init__(self):
        """
        Initialize the Auth class with a DB instance.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with the provided email and password.

        Args:
            email (str): The user's email address.
            password (str): The user's plain password.

        Returns:
            User: The created User object.

        Raises:
            ValueError: If the email is already registered.
        """
        try:
            # Check if the user already exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # If the user does not exist, hash the password & create a new user
            hashed_password = bcrypt.hashpw(password.encode('utf-8'),
                                            bcrypt.gensalt())
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate login credentials by checking if the provided email exists
        and if the provided password matches the stored hashed password.

        Args:
            email (str): The user's email address.
            password (str): The user's plain password.

        Returns:
            bool: True if the login is valid, False otherwise.
        """
        try:
            user: Optional[User] = self._db.find_user_by(email=email)
            if user and bcrypt.checkpw(password.encode('utf-8'),
                                       user.hashed_password):
                return True
        except NoResultFound:
            return False
        return False
