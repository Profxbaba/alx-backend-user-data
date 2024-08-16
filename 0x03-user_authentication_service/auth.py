#!/usr/bin/env python3
"""
This module provides authentication methods, including password hashing.
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password string using bcrypt & returns hashed password as bytes.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted and hashed password.
    """
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
