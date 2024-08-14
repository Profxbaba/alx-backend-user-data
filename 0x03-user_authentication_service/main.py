#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

my_db = DB()

# Add a user to the database
user = my_db.add_user("test@test.com", "PwdHashed")
print(user.id)  # Should print the ID of the newly created user

# Find the user by email
find_user = my_db.find_user_by(email="test@test.com")
print(find_user.id)  # Should print the same ID as above

# Try to find a non-existing user by email
try:
    find_user = my_db.find_user_by(email="test2@test.com")
    print(find_user.id)
except NoResultFound:
    print("Not found")  # Should print "Not found"

# Try to find a user with an invalid filter
try:
    find_user = my_db.find_user_by(no_email="test@test.com")
    print(find_user.id)
except InvalidRequestError:
    print("Invalid")  # Should print "Invalid"
