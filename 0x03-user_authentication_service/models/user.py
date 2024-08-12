#!/usr/bin/env python3
"""
User model definition.
"""

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """User class representing a user in the system."""
    
    __tablename__ = 'users'
    
    email = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    
    def __init__(self, email: str, password: str):
        """Initialize a new User object.

        Args:
            email (str): The email of the user.
            password (str): The hashed password of the user.
        """
        self.email = email
        self.password = password
