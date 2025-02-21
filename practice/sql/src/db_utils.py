import psycopg2

# Database connection parameters
DB_NAME = "dvdrental"
DB_USER = "postgres"
DB_PASSWORD = "<password>"
DB_HOST = "localhost"  # or your PostgreSQL server IP
DB_PORT = "5432"  # Default PostgreSQL port

def execute(query):
    # Establish the connection
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("Connected to the database successfully!")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute a simple query
    cursor.execute(query)

    # Fetch and print the result
    results = cursor.fetchall()
  
    # Close the cursor and connection
    cursor.close()
    conn.close()
    return results
