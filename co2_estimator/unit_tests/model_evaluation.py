import joblib
from sklearn.model_selection import cross_val_score
import pandas as pd
import sys

data = pd.read_parquet(r"eval_dataset.parquet")
Y = data.pop("co2_tailpipe_for_fuel_type1_gpkm")
X = data
co2_estimator = joblib.load("../development/model/co2_emissions.joblib")

r2_cross_val = cross_val_score(co2_estimator, X, Y, cv = 7) # this returns a list of values
r2_mean = r2_cross_val.mean()
r2_std = r2_cross_val.std()

RMSE_cross_val = -1*cross_val_score(co2_estimator, X, Y, cv = 7, scoring='neg_root_mean_squared_error') # this returns a list of values
RMSE_mean = RMSE_cross_val.mean()
RMSE_std = RMSE_cross_val.std()

r2_threshold = 0.85
RMSE_threshold = 50


print(f"CO2 estimator model r2 score: {r2_mean}, std: {r2_std}")
print(f"CO2 estimator model MSE: {RMSE_mean}, std: {RMSE_std}")

if (r2_mean < r2_threshold) | (RMSE_mean > 50):
    print(f"""CI failed, r2_scores or RMSE are lower than 
          thresholds: {r2_threshold} and {RMSE_threshold}, 
          respectively""")
    sys.exit(1)

else: print("CO2 emission estimator model evaluation OK!")
