import os
import mysql.connector
from mysql.connector import errorcode


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to the database using credentials from environment variables.

    Returns:
        mysql.connector.connection.MySQLConnection: A MySQL connection object.
    """
    try:
        connection = mysql.connector.connect(
            user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
            password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
            host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
            database=os.getenv('PERSONAL_DATA_DB_NAME')
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
