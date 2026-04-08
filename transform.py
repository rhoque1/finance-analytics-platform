import pandas as pd

# 1. Load the raw data
file_path = 'data/raw/chase_checking.csv'
print(f"Loading data from: {file_path}...")

df = pd.read_csv(file_path)

# 2. Print the first 5 rows to verify
print("\n--- First 5 Rows of Your Chase Data ---")
print(df.head())

# 3. Clean up the column names (make them lowercase, replace spaces with underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 4. Convert 'posting_date' from text to actual Date objects
df['posting_date'] = pd.to_datetime(df['posting_date'])

# 5. Drop the 'check_or_slip_#' column since it's mostly empty and not useful for our dashboard
if 'check_or_slip_#' in df.columns:
    df = df.drop(columns=['check_or_slip_#'])

print("\n--- After Step 1 Transformations ---")
print("Data Types:\n", df.dtypes)
print("\nColumns Cleaned:", df.columns.tolist())

# 6. Clean up the description: replace multiple spaces with a single space
df['description'] = df['description'].str.replace(r'\s+', ' ', regex=True).str.strip()

# 7. Fix the balance column: strip whitespace and convert to numeric (blanks become NaN)
if df['balance'].dtype == 'object' or df['balance'].dtype == 'str':
    df['balance'] = pd.to_numeric(df['balance'].astype(str).str.strip(), errors='coerce')

print("\n--- After Step 2 Transformations ---")
print("Data Types:\n", df.dtypes)
print("\nCleaned Descriptions (First 5):")
print(df[['description', 'balance']].head())

# --- ADD THIS TO THE BOTTOM OF transform.py ---

import os

# 8. Load the master mapping file
print("\nLoading Category Mapping...")
mapping_df = pd.read_csv('data/merchant_mapping.csv')

# 9. Merge the mapping with our transactions

# A 'left' join ensures we keep all transactions, even if a merchant isn't mapped yet
df = pd.merge(df, mapping_df, on='description', how='left')

# 10. Tag anything that slipped through as 'Uncategorized'
df['category'] = df['category'].fillna('Uncategorized')

print("\n--- Categorization Complete ---")
print("Here is your spending breakdown:")
print(df['category'].value_counts())

# 8. Ensure the processed directory exists
os.makedirs('data/processed', exist_ok=True)

# 9. Save the cleaned data to a new CSV
processed_path = 'data/processed/cleaned_chase_checking.csv'
df.to_csv(processed_path, index=False)

print(f"\nSUCCESS! Cleaned data saved to: {processed_path}")

