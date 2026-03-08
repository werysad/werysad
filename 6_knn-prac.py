import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

# Load dataset
df = pd.read_csv("Iris.csv")

print(df.head())

##KNN checks the nearest neighbors and predicts the value of Y based on them.
# Convert text columns to numeric (only when feature columns contain text)
#df = pd.get_dummies(df, drop_first=True)

# Target column
y = df['Species']

# Features
X = df.drop(['Id','Species'], axis=1)
#or X = [['hana', 'hisdjm','kkpl']]

# Train KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Predict classes
predicted = model.predict(X)

# Expected values
expected = y

# Accuracy
print("Accuracy:", model.score(X, y))

# Detailed report
print(metrics.classification_report(expected, predicted))

# Confusion matrix
print(metrics.confusion_matrix(expected, predicted))

# Visualization (optional)
sns.scatterplot(x=df['PetalLengthCm'], y=df['Species'], hue=y)
plt.title("KNN Classification")
plt.show()

#----------------iris--------------
#Iris Data Set
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn import datasets
# from sklearn import metrics
# from sklearn.neighbors import KNeighborsClassifier

# # Load dataset
# iris = datasets.load_iris()

# # Convert to DataFrame
# df = pd.DataFrame(np.c_[iris.data, iris.target],
#                   columns=iris.feature_names + ['target'])

# # Show dataset
# print(df.head())

# # Count class values
# print(df["target"].value_counts())

# # Visualize classes
# sns.FacetGrid(df, hue="target", height=6).map(
#     plt.scatter, "petal length (cm)", "petal width (cm)"
# ).add_legend()
# plt.show()

# # Train KNN model
# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(iris.data, iris.target)

# # Predict classes
# predicted = model.predict(iris.data)
# expected = iris.target

# # Accuracy
# print("Accuracy:", model.score(iris.data, iris.target))

# # Detailed report
# print(metrics.classification_report(expected, predicted))

# # Confusion matrix
# print(metrics.confusion_matrix(expected, predicted))

