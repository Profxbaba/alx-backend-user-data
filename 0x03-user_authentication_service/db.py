#!/usr/bin/env python3
"""
Module for database interactions.
"""

from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model for the users table.
    """
    __tablename__ = 'users'
    email = Column(String(120), primary_key=True)
    password = Column(String(255))
    session_id = Column(String(36))


class DB:
    """
    Class to handle database operations.
    """

    def __init__(self):
        """
        Initialize the DB class and create a database session.
        """
        self.engine = create_engine('sqlite:///database.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def add_user(self, email: str, password: bytes) -> None:
        """
        Add a new user to the database.

        Args:
            email (str): The user's email.
            password (bytes): The hashed password.
        """
        new_user = User(email=email, password=password)
        self.session.add(new_user)
        self.session.commit()

    def get_user_by_email(self, email: str) -> User:
        """
        Retrieve a user from the database by email.

        Args:
            email (str): The user's email.

        Returns:
            User: The user object if found, None otherwise.
        """
        return self.session.query(User).filter_by(email=email).first()

    def update_user_session(self, email: str, session_id: str) -> None:
        """
        Update the session ID for a user.

        Args:
            email (str): The user's email.
            session_id (str): The new session ID.
        """
        user = self.get_user_by_email(email)
        if user:
            user.session_id = session_id
            self.session.commit()
