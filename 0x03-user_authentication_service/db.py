#!/usr/bin/env python3
"""
DB class to interact with the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import Base, User


class DB:
    """Database class for handling user data."""

    def __init__(self):
        """Initialize the database connection and session."""
        self.engine = create_engine('sqlite:///mydatabase.db')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)

    def get_user_by_email(self, email: str) -> User:
        """Retrieve a user by email.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            User: The User object if found, else None.
        """
        return self.session.query(User).filter_by(email=email).first()

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database.

        Args:
            email (str): The email of the new user.
            hashed_password (str): The hashed password of the new user.

        Returns:
            User: The newly created User object.
        """
        user = User(email=email, password=hashed_password)
        self.session.add(user)
        self.session.commit()
        return user
