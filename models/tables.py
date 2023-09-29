import psycopg2
from config.config_secrets import DATABASE_CREDENTIALS

# Function to create the 'Stories' table with the specified schema
def create_stories_table():
    try:
        conn = psycopg2.connect(**DATABASE_CREDENTIALS)

        # Open a cursor to execute SQL commands
        cursor = conn.cursor()

        # SQL command to create the 'Stories' table
        create_table_query = '''
        CREATE TABLE mythology (
            Culture_name TEXT,
            Title TEXT,
            Text TEXT
        );
        '''

        # Execute the SQL command to create the table
        cursor.execute(create_table_query)
        conn.commit()

        print("Table 'Stories' created successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL or executing the SQL command:", error)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Function to insert data into the 'Stories' table
def insert_data_into_stories_table(culture_name, title, text):
    try:
        conn = psycopg2.connect(**DATABASE_CREDENTIALS)

        # Open a cursor to execute SQL commands
        cursor = conn.cursor()

        # SQL command to insert data into the 'Stories' table
        insert_query = '''
        INSERT INTO mythology (Culture_name, Title, Text)
        VALUES (%s, %s, %s);
        '''

        # Execute the SQL command to insert data
        cursor.execute(insert_query, (culture_name, title, text))
        conn.commit()

        print(f"mythology '{title}' inserted successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL or inserting data:", error)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    create_stories_table()

    # Example of inserting a story into the 'Stories' table
    example_title = "The Tale of the Mysterious Land"
    example_text = "Once upon a time, in a realm far away..."
    insert_data_into_stories_table("Culture1", example_title, example_text)
