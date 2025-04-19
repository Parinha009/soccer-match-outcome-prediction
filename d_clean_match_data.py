import sqlite3
import pandas as pd

# Connect to your database
conn = sqlite3.connect('a_database.sqlite')

# Read Match table into DataFrame
matches = pd.read_sql_query("SELECT * FROM Match", conn)

# Show first few rows
print(matches.head())

# Close the connection
conn.close()


# Drop unnecessary columns
columns_to_drop = ['id', 'country_id', 'league_id', 'season', 'stage', 'date', 'match_api_id', 'home_team_api_id', 'away_team_api_id']
matches.drop(columns=columns_to_drop, inplace=True)

# Drop columns that have too many missing values
threshold = 0.5  # 50% missing -> drop
matches = matches.loc[:, matches.isnull().mean() < threshold]

# Drop rows with any missing values (optional: safe way)
matches.dropna(inplace=True)

# Show the cleaned data
print(matches.head())

# Save to a CSV file
matches.to_csv('cleaned_matches.csv', index=False)
