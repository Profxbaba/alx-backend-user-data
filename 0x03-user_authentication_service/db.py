#!/usr/bin/env python3
"""
DB module for managing user database interactions.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User
from typing import Dict, Any


class DB:
    """DB class for managing database interactions."""

    def __init__(self) -> None:
        """Initialize a new DB instance."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database.

        Args:
            email (str): The user's email address.
            hashed_password (str): The hashed password for the user.

        Returns:
            User: The newly added User object.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs: Dict[str, Any]) -> User:
        """Find a user by arbitrary keyword arguments.

        Args:
            kwargs (Dict[str, Any]): The attributes to filter by.

        Returns:
            User: The first user found matching the criteria.

        Raises:
            NoResultFound: If no user is found.
            InvalidRequestError: If an invalid attribute is provided.
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound
            return user
        except InvalidRequestError:
            raise InvalidRequestError
        except NoResultFound:
            raise NoResultFound

    def update_user(self, user_id: int, **kwargs: Dict[str, Any]) -> None:
        """Update user attributes.

        Args:
            user_id (int): The ID of the user to update.
            kwargs (Dict[str, Any]): The attributes to update.

        Raises:
            ValueError: If an invalid attribute is provided.
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"{key} is not a valid attribute of User")
            setattr(user, key, value)
        self._session.commit()
