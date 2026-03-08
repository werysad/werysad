#Supervised learning algorithm used for classification that finds the optimal hyperplane separating different classes.

# SVM – IRIS DATASET (LOCAL CSV)

import pandas as pd
from sklearn.svm import SVC
from sklearn import metrics

# Load dataset
df = pd.read_csv("Iris.csv")

print(df.head())

# Features
X = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]

# Target
y = df['Species']


# ======================
# LINEAR KERNEL # Linear → straight boundary
# ======================
print("\n--- Linear Kernel ---")

model = SVC(kernel='linear', C=0.1)
model.fit(X, y)

pred = model.predict(X)

print("Accuracy:", model.score(X, y))
print(metrics.classification_report(y, pred))
print(metrics.confusion_matrix(y, pred))


# ======================
# POLYNOMIAL KERNEL # Polynomial → curved boundary

# ======================
print("\n--- Polynomial Kernel ---")

model = SVC(kernel='poly', degree=3, C=0.1)
model.fit(X, y)

pred = model.predict(X)

print("Accuracy:", model.score(X, y))
print(metrics.classification_report(y, pred))
print(metrics.confusion_matrix(y, pred))


# ======================
# RBF KERNEL # RBF → flexible boundary
# ======================
print("\n--- RBF Kernel ---")

model = SVC(kernel='rbf', C=0.1)
model.fit(X, y)

pred = model.predict(X)

print("Accuracy:", model.score(X, y))
print(metrics.classification_report(y, pred))
print(metrics.confusion_matrix(y, pred))


# # SVM – IRIS DATASET (BUILT-IN)

# from sklearn.datasets import load_iris
# from sklearn.svm import SVC
# from sklearn import metrics

# # Load dataset
# iris = load_iris()
# X = iris.data
# y = iris.target


# # ======================
# # LINEAR KERNEL
# # ======================
# print("\n--- Linear Kernel ---")

# model = SVC(kernel='linear', C=0.1)
# model.fit(X, y)

# pred = model.predict(X)

# print("Accuracy:", model.score(X, y))
# print(metrics.classification_report(y, pred))
# print(metrics.confusion_matrix(y, pred))


# # ======================
# # POLYNOMIAL KERNEL
# # ======================
# print("\n--- Polynomial Kernel ---")

# model = SVC(kernel='poly', degree=3, C=0.1)
# model.fit(X, y)

# pred = model.predict(X)

# print("Accuracy:", model.score(X, y))
# print(metrics.classification_report(y, pred))
# print(metrics.confusion_matrix(y, pred))


# # ======================
# # RBF KERNEL
# # ======================
# print("\n--- RBF Kernel ---")

# model = SVC(kernel='rbf', C=0.1)
# model.fit(X, y)

# pred = model.predict(X)

# print("Accuracy:", model.score(X, y))
# print(metrics.classification_report(y, pred))
# print(metrics.confusion_matrix(y, pred))