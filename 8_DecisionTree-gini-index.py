import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

iris = pd.read_csv("Iris.csv")

X = iris[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y = iris['Species']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#gini-index=measure of node impurity used to choose the best split.
model = DecisionTreeClassifier()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("Accuracy:",accuracy_score(y_test,y_pred))

tree.plot_tree(model,feature_names=X.columns,class_names=model.classes_,filled=True)
plt.show()


# -----------------iris code----------------------
# import pandas as pd
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score
# from sklearn import tree
# import matplotlib.pyplot as plt

# # Load built-in Iris dataset
# iris = load_iris()

# # Convert to DataFrame
# df = pd.DataFrame(iris.data, columns=iris.feature_names)
# df["Species"] = iris.target

# print(df.head())

# # Features and target
# X = df[iris.feature_names]
# y = df["Species"]

# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# 
# model = DecisionTreeClassifier()

# # Train model
# model.fit(X_train, y_train)

# # Prediction
# y_pred = model.predict(X_test)

# # Accuracy
# print("Accuracy:", accuracy_score(y_test, y_pred))

# # Plot decision tree
# tree.plot_tree(
#     model,
#     feature_names=iris.feature_names,
#     class_names=iris.target_names,
#     filled=True
# )

# plt.show()