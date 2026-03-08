import pandas as pd 
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error,mean_squared_error
import matplotlib.pyplot as plt

#predicts a value using two input features
def mlr(data,labels,target,to_predict):
    #load the data 
    data = pd.read_csv("data.csv")
    X = data[labels].values
    Y = data[target].values
    
    #train the linear regression model 
    regression = linear_model.LinearRegression()
    regression.fit(X,Y)
    
    #print regression coeffecients
    print(f"Regression Coeffecients : {regression.coef_}")
    
    #Predict for new data
    predicted = regression.predict(to_predict)
    print(f"Prediction for new data : {predicted}")
    
    #predictfor the training data
    y_predicted = regression.predict(X)
    print(f"Predicted Y:\n{y_predicted}")
    
    #Calculate error metrics
    mae = mean_absolute_error(y_true=Y,y_pred=y_predicted)
    mse = mean_squared_error(y_true=Y,y_pred=y_predicted)
    
    print(f"Mean absolute error (MAE): {mae}")
    print(f"Mean squared error (MSE) : {mse}")
    
    #visualization 3d scatter plot
    fig =plt.figure(figsize=(10,8))
    
    ax = fig.add_subplot(111,projection='3d')
    x1 = data[labels[0]]
    x2 = data[labels[1]]
    y = data[target]
    
    ax.scatter(x1,x2,y,c="blue",marker='o')
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_zlabel(target)

    
    plt.show()
    
    #Select the coloums and target from question 
mlr('data.csv',['Weight','Volume'],'CO2',[[3300,1300]])
