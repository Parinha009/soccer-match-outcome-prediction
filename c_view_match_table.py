import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('database.sqlite')

# Read the 'Match' table into a DataFrame
matches = pd.read_sql_query("SELECT * FROM Match", conn)

# Show the first 5 rows
print(matches.head())

# Close the connection
conn.close()
