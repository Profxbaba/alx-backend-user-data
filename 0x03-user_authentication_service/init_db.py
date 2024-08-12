#!/usr/bin/env python3
"""
Script to initialize the database schema.
"""

from db import DB
from models.user import Base

def initialize_database():
    """Initialize the database and create tables."""
    db = DB()
    Base.metadata.create_all(db.engine)

if __name__ == "__main__":
    initialize_database()
