import pandas as pd

# Load your cleaned data
df = pd.read_csv('data/processed/cleaned_chase_checking.csv')

# Get a list of every unique description
unique_merchants = df['description'].unique()

print(f"Found {len(unique_merchants)} unique merchants. Here is the list:\n")
for merchant in unique_merchants:
    print(merchant)