import os
import psycopg2
from config.config_secrets import DATABASE_CREDENTIALS
from utils.validators import validate_directory, validate_file
from logger.logger import log_error
from models.tables import create_stories_table, insert_data_into_stories_table


database_info = DATABASE_CREDENTIALS
local_directory = '/Users/francinasimone/Desktop/DreamApp1/Starlight/First_People/'

class DatabaseConnection:
    def __init__(self, db_info):
        self.db_info = db_info
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_info)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

def insert_data(culture_name, title, text):
    query = '''
    INSERT INTO mythology (Culture_name, Title, Text)
    VALUES (%s, %s, %s);
    '''
    with DatabaseConnection(database_info) as cursor:
        cursor.execute(query, (culture_name, title, text))

def store_stories_in_database(folder_names, directory):
    if not validate_directory(directory):
        return

    for culture_name in folder_names:
        culture_folder_path = os.path.join(directory, culture_name)

        # This is the primary check we're adding
        if not validate_directory(culture_folder_path):
            continue

        for story_file in os.listdir(culture_folder_path):
            story_path = os.path.join(culture_folder_path, story_file)

            # Here, we're also ensuring we only read valid files
            if os.path.isfile(story_path):
                with open(story_path, 'r') as f:
                    story_content = f.read()
                insert_data(culture_name, story_file, story_content)

folder_names = os.listdir(local_directory)  # We assume that all items are folders for simplicity.
store_stories_in_database(folder_names, local_directory)