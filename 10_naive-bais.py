import pandas as pd
import numpy as np
from sklearn import datasets, metrics
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

# Load dataset
iris = datasets.load_iris()

# Convert to DataFrame 
df = pd.DataFrame(
    np.c_[iris.data, iris.target],
    columns=iris.feature_names + ['target']
)
print(df.head())

X = iris.data
y = iris.target


# ======================
# GAUSSIAN NAIVE BAYES
# ======================
print("\n--- Gaussian Naive Bayes ---")

#GaussianNB assumes features follow continuous numbers normal distribution 
model = GaussianNB()
model.fit(X, y)

pred = model.predict(X)

print("Gaussian Accuracy:", model.score(X, y))
print(metrics.classification_report(y, pred))
print(metrics.confusion_matrix(y, pred))


# ======================
# MULTINOMIAL NAIVE BAYES
# ======================
print("\n--- Multinomial Naive Bayes ---")

model = MultinomialNB()
model.fit(X, y)

#features represent counts or frequencies
pred = model.predict(X)

print("Multinomial Accuracy:", model.score(X, y))
print(metrics.classification_report(y, pred))
print(metrics.confusion_matrix(y, pred))


# ======================
# BERNOULLI NAIVE BAYES
# ======================
print("\n--- Bernoulli Naive Bayes ---")
#BernoulliNB features represent counts or frequencies
model = BernoulliNB()
model.fit(X, y)

pred = model.predict(X)

print("Bernoulli Accuracy:", model.score(X, y))
print(metrics.classification_report(y, pred))
print(metrics.confusion_matrix(y, pred))


#------------------custom csv------------------------------
# import pandas as pd
# from sklearn import metrics
# from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

# # Load dataset from local CSV
# df = pd.read_csv("Iris.csv")

# print(df.head())

# # Features (remove Id and Species)
# X = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]

# # Target
# y = df['Species']


# # ======================
# # GAUSSIAN NAIVE BAYES
# # ======================
# print("\n--- Gaussian Naive Bayes ---")

# model = GaussianNB()
# model.fit(X, y)

# pred = model.predict(X)

# print("Gaussian Accuracy:", model.score(X, y))
# print(metrics.classification_report(y, pred))
# print(metrics.confusion_matrix(y, pred))


# # ======================
# # MULTINOMIAL NAIVE BAYES
# # ======================
# print("\n--- Multinomial Naive Bayes ---")

# model = MultinomialNB()
# model.fit(X, y)

# pred = model.predict(X)

# print("Multinomial Accuracy:", model.score(X, y))
# print(metrics.classification_report(y, pred))
# print(metrics.confusion_matrix(y, pred))


# # ======================
# # BERNOULLI NAIVE BAYES
# # ======================
# print("\n--- Bernoulli Naive Bayes ---")

# model = BernoulliNB()
# model.fit(X, y)

# pred = model.predict(X)

# print("Bernoulli Accuracy:", model.score(X, y))
# print(metrics.classification_report(y, pred))
# print(metrics.confusion_matrix(y, pred))