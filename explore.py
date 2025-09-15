# explore.py
import pandas as pd

# Load the CSV we created
df = pd.read_csv("sales_sample.csv", parse_dates=["date"])

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Show summary statistics
print("\nSummary statistics:")
print(df["units_sold"].describe())

# Save a cleaned version
df.to_csv("sales_sample_clean.csv", index=False)
print("\n✅ Cleaned CSV saved as sales_sample_clean.csv")
