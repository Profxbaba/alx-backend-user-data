#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """
    DB class
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    def _session(self) -> Session:
        """
        Memoize session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database.

        Args:
            email (str): The user's email address.
            hashed_password (str): The user's hashed password.

        Returns:
            User: The User object that was created.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        session = self._session()
        session.add(new_user)
        session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by an arbitrary attribute.

        Args:
            kwargs (dict): A dictionary of the attribute to filter by.

        Returns:
            User: The User object that matches the criteria.

        Raises:
            NoResultFound: If no user is found with the given criteria.
            InvalidRequestError: If the query is invalid.
        """
        session = self._session()
        try:
            return session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound(f"No user found with the criteria: {kwargs}")
        except InvalidRequestError:
            raise InvalidRequestError(
                    f"Invalid query with the criteria: {kwargs}"
            )

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user's attributes.

        Args:
            user_id (int): The ID of the user to update.
            kwargs (dict): A dictionary of the attributes to update.
        Returns:
            None

        Raises:
            ValueError: If an attribute does not exist on the User model.
        """
        session = self._session()
        # Locate the user using find_user_by method
        user = self.find_user_by(id=user_id)

        # Loop through the keyword arguments to update user attributes
        for key, value in kwargs.items():
            # Check if the attribute exists on the User model
            if not hasattr(user, key):
                raise ValueError(
                        f"'{key}' is not a valid attribute of the User model"
                )
            # Set the attribute value
            setattr(user, key, value)

        # Commit the changes to the database
        session.commit()
