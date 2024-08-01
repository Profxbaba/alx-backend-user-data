#!/usr/bin/env python3
"""
Filtered Logger module
"""

import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class

    This class formats log records to redact sensitive information.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize RedactingFormatter with fields to redact

        Args:
            fields (List[str]): List of field names whose values should be
                redacted.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format log record with redacted fields

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record with sensitive fields redacted.
        """
        message = record.getMessage()
        for field in self.fields:
            message = re.sub(
                rf'{field}=[^;]*',
                f'{field}={self.REDACTION}',
                message
            )
        return super().format(record)
