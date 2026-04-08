import pandas as pd
import sqlite3

# 1. Load your perfectly clean, categorized data
csv_path = 'data/processed/cleaned_chase_checking.csv'
print(f"Reading clean data from {csv_path}...")
df = pd.read_csv(csv_path)

# 2. Connect to SQLite (this creates the database file automatically)
db_path = 'data/finance.db'
conn = sqlite3.connect(db_path)

# 3. Load the data into a SQL table called 'transactions'
print("Loading data into the SQL database...")
# if_exists='replace' means if you run this twice, it cleanly overwrites the old table
df.to_sql('transactions', conn, if_exists='replace', index=False)

# 4. Prove it worked by asking the database a real SQL question
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM transactions;")
row_count = cursor.fetchone()[0]

print(f"\nSUCCESS! Database created at: {db_path}")
print(f"Total rows loaded into the 'transactions' table: {row_count}")

# 5. Close the door on the way out
conn.close()