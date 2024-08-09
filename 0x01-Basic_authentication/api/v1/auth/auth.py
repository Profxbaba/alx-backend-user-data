#!/usr/bin/env python3
"""
Auth module for managing API authentication.
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """
    Auth class for handling authentication related methods.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required.
        Currently returns False for all paths.

        Args:
        path (str): The path to check.
        excluded_paths (List[str]): A list of paths that are excluded
        from authentication.

        Returns:
            bool: False as the default implementation.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from the request.
        Currently returns None.

        Args:
        request (Request, optional): The Flask request object.
        Defaults to None.

        Returns:
            str: None as the default implementation.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user.
        Currently returns None.

        Args:
        request (Request, optional): The Flask request object.
        Defaults to None.

        Returns:
            TypeVar('User'): None as the default implementation.
        """
        return None
