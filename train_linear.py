import pandas as pd
import numpy as np
import pickle

df = pd.read_csv("sales_sample.csv", parse_dates=["date"])
df = df.sort_values("date")

df["lag_1"] = df["units_sold"].shift(1).fillna(0)

X = np.vstack([np.ones(len(df)), df["lag_1"].values]).T
y = df["units_sold"].values

coef, *_ = np.linalg.lstsq(X, y, rcond=None)
print("Model coefficients:", coef)

preds = X.dot(coef)
mae = np.mean(np.abs(y - preds))
rmse = np.sqrt(np.mean((y - preds)**2))
print(f"MAE: {mae:.2f}, RMSE: {rmse:.2f}")

with open("model_coef.pkl", "wb") as f:
    pickle.dump(coef, f)

print("✅ Model saved to model_coef.pkl")
