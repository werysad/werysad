import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# Load dataset
iris = pd.read_csv("Iris.csv")

print(iris.head())

# Class distribution
print(iris["Species"].value_counts())

# Visualization
sns.scatterplot(x=iris["PetalLengthCm"], y=iris["SepalWidthCm"], hue=iris["Species"])
plt.show()

# Features
X = iris[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]

# Target
y = iris['Species']

# Train model
model = LogisticRegression()
model.fit(X,y)

# Intercept & coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Accuracy
print("Accuracy:", model.score(X,y))

# Prediction
predicted = model.predict(X)
expected = y

# Classification report
print(metrics.classification_report(expected,predicted))

#------------------------iris------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.datasets import load_iris
# from sklearn.linear_model import LogisticRegression
# from sklearn import metrics

# # Load Iris dataset from sklearn
# iris = load_iris()

# # Convert to DataFrame
# df = pd.DataFrame(iris.data, columns=iris.feature_names)
# df["Species"] = iris.target

# print(df.head())

# # Class distribution
# print(df["Species"].value_counts())

# # Visualization
# sns.scatterplot(x=df["petal length (cm)"], y=df["sepal width (cm)"], hue=df["Species"])
# plt.title("Iris Dataset Visualization")
# plt.show()

# # Features
# X = df[iris.feature_names]

# # Target
# y = df["Species"]

# # Train Logistic Regression model
# model = LogisticRegression(max_iter=200)
# model.fit(X, y)

# # Intercept and coefficients
# print("Intercept:", model.intercept_)
# print("Coefficients:", model.coef_)

# # Accuracy
# print("Accuracy:", model.score(X, y))

# # Prediction
# predicted = model.predict(X)
# expected = y

# # Classification report
# print(metrics.classification_report(expected, predicted))

# # Confusion matrix
# print(metrics.confusion_matrix(expected, predicted))