# predict.py
import pickle
import numpy as np

# Load the saved model
with open("model_coef.pkl", "rb") as f:
    coef = pickle.load(f)

# Ask user for input
try:
    lag_1 = float(input("Enter yesterday's sales (lag_1): "))
except ValueError:
    print("❌ Please enter a valid number!")
    exit()

# Make prediction
X = np.array([1.0, lag_1])
pred = float(np.dot(X, coef))

print(f"\nYesterday's sales: {lag_1}")
print(f"Predicted today's sales: {pred:.2f}")
