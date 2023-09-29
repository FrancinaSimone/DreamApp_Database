from logger.logger import log_error
import os
import psycopg2

def validate_directory(path):
    """Checks if a given path is a directory."""
    return os.path.isdir(path)


def validate_file(file_path):
    if not os.path.isfile(file_path):
        log_error(f"File not found: {file_path}")
        return False
    return True