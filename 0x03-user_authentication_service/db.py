#!/usr/bin/env python3
"""
Database module for handling user data.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()


class User(Base):
    """User class representing the users table."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False)


class DB:
    """DB class for interacting with the database."""

    def __init__(self):
        """Initialize the database connection and session."""
        self._engine = create_engine('sqlite:///my_database.db')
        Base.metadata.create_all(self._engine)
        self._session = sessionmaker(bind=self._engine)()

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database.

        Args:
            email (str): The user's email.
            hashed_password (str): The hashed password.

        Returns:
            User: The created User object.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by specific attributes.

        Args:
            **kwargs: Arbitrary keyword arguments representing user attributes.

        Returns:
            User: The found User object.

        Raises:
            NoResultFound: If no user is found with the provided attributes.
        """
        return self._session.query(User).filter_by(**kwargs).one()
