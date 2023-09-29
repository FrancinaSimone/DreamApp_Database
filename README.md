
## Features
- **Configurable Database Connection**: Via `config_secrets.py`, configure your PostgreSQL database credentials.
- **Validators**: Located under `utils/validators.py`, contains utility functions to validate directories and files.
- **Logging**: The `logger/logger.py` takes care of error logging.
- **Database Operations**: `main/main_operations.py` handles all the core database operations like creating tables and inserting data.

## How to Use
1. Make sure PostgreSQL is set up on your machine.
2. Update `config_secrets.py` with your PostgreSQL credentials.
3. Install the dependencies from `requirements.txt`.
4. Run `main_operations.py` to create the `mythology` table and insert an example story.

## Dependencies
- PostgreSQL
- psycopg2

To install all dependencies, run:
