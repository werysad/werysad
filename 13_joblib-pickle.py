import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle
import joblib
data = pd.read_csv("tips.csv")

print("Dataset Preview:\n")
print(data.head())

columns_to_drop = ["Payer Name", "CC Number", "Payment ID"]

for col in columns_to_drop:
    if col in data.columns:
        data = data.drop(col, axis=1)

data = pd.get_dummies(data, drop_first=True)
X = data.drop("tip", axis=1)
y = data["tip"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#normal accuracy
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print("\nR2 Score:", r2)

# Save model using Joblib
joblib.dump(model, "tips_model_joblib.pkl")
print("Model saved using Joblib!")
# Load model using Joblib
loaded_joblib_model = joblib.load("tips_model_joblib.pkl")
joblib_r2 = loaded_joblib_model.score(X_test, y_test)
print("Loaded Joblib Model R2 Score:", joblib_r2)

# Save model using Pickle 
pd.to_pickle(model, "tips_model_pickle.pkl")
print("Model saved using Pickle")
# Load model using Pickle 
loaded_easy_pickle_model = pd.read_pickle("tips_model_pickle.pkl")
easy_pickle_r2 = loaded_easy_pickle_model.score(X_test, y_test)
print("Loaded Easy Pickle Model R2 Score:", easy_pickle_r2)