#!/usr/bin/env python3
"""
This module provides a logger for handling user data with PII redaction.
"""

import logging
import re
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class.
    """

    REDACTION = "***"
    FORMAT = "[USER_DATA] %(name)s %(levelname)s %(asctime)s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def redact(self, message: str) -> str:
        """
        Redacts fields in the message.
        """
        for field in self.fields:
            message = re.sub(
                f"(?<={field}=)[^{self.SEPARATOR}]*", self.REDACTION, message
            )
        return message

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record and redacts PII fields.
        """
        message = super(RedactingFormatter, self).format(record)
        return self.redact(message)


def get_logger() -> logging.Logger:
    """
    Returns a logger named "user_data" with INFO level, no propagation,
    and a StreamHandler with RedactingFormatter.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
