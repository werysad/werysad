import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.calibration import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn import metrics

# Load dataset
iris = pd.read_csv("C:/Users/darpa/OneDrive/Desktop/ML/Iris.csv")
# Encode target column
le = LabelEncoder()
iris['Species'] = le.fit_transform(iris['Species'])

# Features and target
X = iris[['SepalLengthCm', 'SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y = iris['Species']


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
regressor = RandomForestRegressor(n_estimators=20, random_state=0)
regressor.fit(X_train, y_train)

# Prediction
Y_pred = regressor.predict(X_test)

# Metrics
print('Mean Absolute Error:\n', metrics.mean_absolute_error(y_test, Y_pred))
print('\nMean Squared Error:\n', metrics.mean_squared_error(y_test, Y_pred))
print('\nRoot Mean Squared Error:\n',
      np.sqrt(metrics.mean_squared_error(y_test, Y_pred)))

classifier = RandomForestClassifier(n_estimators=2,random_state = 0)
classifier.fit(X_train,y_train)

Y_pred = classifier.predict(X_test)
print('Confusion matrix: \n ',metrics.confusion_matrix(y_test,Y_pred))
print('\n Classification report : \n ',metrics.classification_report(y_test,Y_pred))
print('\n Accuracy scoree: \n',accuracy_score (y_test,Y_pred))

#uses Multiple decision tree
