import psycopg2

# Azure PostgreSQL connection details
HOST = "jawa.postgres.database.azure.com"
DBNAME = "postgres"
USER = "jawa01"
PASSWORD = "welcome5005!"
PORT = 5432

try:
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(
        host=HOST,
        dbname=DBNAME,
        user=USER,
        password=PASSWORD,
        port=PORT,
        sslmode='require'  # Azure requires SSL
    )

    print("Connected to Azure PostgreSQL!")

    # Create a cursor object
    cur = conn.cursor()

    # Create a sample table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            email VARCHAR(50)
        )
    """)
    conn.commit()
    print("Table created successfully.")

    # Insert sample data
    cur.execute("""
        INSERT INTO users (name, email)
        VALUES (%s, %s)
    """, ("Alice", "alice@example.com"))
    conn.commit()
    print("Data inserted successfully.")

    # Query data
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    print("Data from table:")
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()
    print("Connection closed.")

except Exception as e:
    print("Error:", e)
