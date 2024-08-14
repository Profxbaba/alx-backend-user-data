#!/usr/bin/env python3
"""
DB module for interacting with the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import User
from typing import TypeVar, Dict, Any


class DB:
    """DB class for interacting with the database."""

    def __init__(self) -> None:
        """Initialize a new DB instance."""
        self._engine = create_engine("sqlite:///a.db")
        self._Session = sessionmaker(bind=self._engine)

    def add_user(self, email: str, hashed_password: str) -> TypeVar('User'):
        """
        Adds a new user to the database.

        Args:
            email (str): The user's email address.
            hashed_password (str): The user's hashed password.

        Returns:
            User: The newly created user.
        """
        session = self._Session()
        new_user = User(email=email, hashed_password=hashed_password)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        session.close()
        return new_user

    def find_user_by(self, **kwargs: Dict[str, Any]) -> TypeVar('User'):
        """
        Finds the first user in the database that matches the criteria 
        provided by keyword arguments.

        Args:
            kwargs (dict): Arbitrary keyword arguments to filter users.

        Returns:
            User: The first user that matches the criteria.

        Raises:
            NoResultFound: If no user matches the criteria.
            InvalidRequestError: If the query is invalid.
        """
        if not kwargs:
            raise InvalidRequestError("No filter arguments provided")

        session = self._Session()

        try:
            user = session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound("No user found with the given parameters")
            return user
        except InvalidRequestError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update_user(self, user_id: int, **kwargs: Dict[str, Any]) -> None:
        """
        Updates a user's attributes based on the provided keyword arguments.

        Args:
            user_id (int): The ID of the user to update.
            kwargs (dict): Arbitrary keyword arguments representing the user's
                           attributes to update.

        Raises:
            ValueError: If any of the kwargs do not correspond to a valid 
                        user attribute.
        """
        session = self._Session()

        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if not hasattr(user, key):
                    raise ValueError(f"{key} is not a valid attribute of User")
                setattr(user, key, value)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
