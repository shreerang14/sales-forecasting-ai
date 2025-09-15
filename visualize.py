# visualize.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle

# Load dataset
df = pd.read_csv("sales_sample_clean.csv", parse_dates=["date"])

# Load the trained model
with open("model_coef.pkl", "rb") as f:
    coef = pickle.load(f)

# Create lag feature (yesterday’s sales)
df = df.sort_values("date")
df["lag_1"] = df["units_sold"].shift(1).fillna(0)

# Predictions
X = np.vstack([np.ones(len(df)), df["lag_1"].values]).T
df["predicted"] = X.dot(coef)

# Plot actual vs predicted
plt.figure(figsize=(12,6))
plt.plot(df["date"], df["units_sold"], label="Actual Sales", color="blue")
plt.plot(df["date"], df["predicted"], label="Predicted Sales", color="red", linestyle="--")
plt.title("Actual vs Predicted Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Units Sold")
plt.legend()
plt.grid(True)

# Save chart
plt.savefig("sales_vs_predicted.png")
print("✅ Chart saved as sales_vs_predicted.png")
