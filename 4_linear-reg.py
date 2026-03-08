import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("Salary_Data.csv")

# Remove missing values
df = df.dropna()

# Preview data
print(df.head())
#summary mean avg
print(df.describe())

# Visualization
plt.scatter(df['Years of Experience'], df['Salary'])
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience")
plt.show()

# Split X and Y
X = df[['Years of Experience']]
y = df['Salary']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Print regression equation
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

# Predict
y_pred = model.predict(X_test)

# Visualization of regression line
plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred, color='red')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression Model")
plt.show()

# R² Score
print("R2 Score:", r2_score(y_test, y_pred))


# ----------------iris------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score

# # Load built-in Iris dataset
# iris = load_iris()

# # Convert to DataFrame
# df = pd.DataFrame(iris.data, columns=iris.feature_names)

# # Preview data
# print(df.head())

# # Summary statistics
# print(df.describe())

# # Visualization
# plt.scatter(df['petal length (cm)'], df['petal width (cm)'])
# plt.xlabel("Petal Length (cm)")
# plt.ylabel("Petal Width (cm)")
# plt.title("Petal Length vs Petal Width")
# plt.show()

# # Split X and Y
# X = df[['petal length (cm)']]
# y = df['petal width (cm)']

# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=0
# )

# # Train model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Print regression equation
# print("Coefficient:", model.coef_)
# print("Intercept:", model.intercept_)

# # Predict
# y_pred = model.predict(X_test)

# # Visualization of regression line
# plt.scatter(X_test, y_test)
# plt.plot(X_test, y_pred)
# plt.xlabel("Petal Length (cm)")
# plt.ylabel("Petal Width (cm)")
# plt.title("Linear Regression Model")
# plt.show()

# # R² Score
# print("R2 Score:", r2_score(y_test, y_pred))