# data_gen.py
import csv
from datetime import date, timedelta
import random

# Start date
start = date(2025, 1, 1)

# Empty list to collect rows
rows = []

# Generate 120 days of fake sales
for i in range(120):
    d = start + timedelta(days=i)
    units = max(0, int(10 + random.gauss(0, 3)))  # random sales number
    rows.append([d.isoformat(), "SKU1", "StoreA", units])

# Save to CSV file
with open("sales_sample.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "sku_id", "store_id", "units_sold"])
    writer.writerows(rows)

print("✅ sales_sample.csv created in your folder")
dir