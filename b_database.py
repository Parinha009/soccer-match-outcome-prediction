import sqlite3

# Connect to your database (simple because your .sqlite file is already inside the ML-demo folder)
conn = sqlite3.connect('database.sqlite')

# Create a cursor
cursor = conn.cursor()

# Show all the tables inside the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print the tables
print("Tables inside database:", tables)
