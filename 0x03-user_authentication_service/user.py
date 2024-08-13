#!/usr/bin/env python3
"""
User model for the database
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """User class for SQLAlchemy model"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False)
    hashed_password = Column(String(128), nullable=False)
