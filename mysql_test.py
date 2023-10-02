import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)

# Create a cursor object
cursor = conn.cursor()

# Execute a SELECT query and print each row to the console
cursor.execute("SELECT * FROM customers ORDER BY customer_id")
for row in cursor.fetchall():
    print(row)

# Execute an UPDATE query
cursor.execute("UPDATE customers SET customer_name = 'Something' WHERE customer_id = 1")

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
