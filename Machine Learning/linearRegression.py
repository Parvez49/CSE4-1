# -*- coding: utf-8 -*-
"""LinearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qh3EKqohWZzmHZeNHdipyIBRHizq0O-r
"""

import numpy as np


def r2_score(y_true, y_pred):
    corr_matrix = np.corrcoef(y_true, y_pred)
    #print(corr_matrix)
    #print(corr_matrix)
    corr = corr_matrix[0, 1]# same as corr_matrix[0][1]
    #print(corr_matrix[0][1])
    return corr ** 2


class LinearRegression:
    def __init__(self, learning_rate=0.001, n_iters=2):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):

        #print(X.shape) #--> (80,1)
        n_samples, n_features = X.shape
        


        # init parameters
        self.weights = np.zeros(n_features)
        #print(self.weights.shape)
        #print(type(self.weights)) #--> numpy.ndarray #self.weights=[0.]
        self.bias = 0

        # gradient descent
        #print(np.dot(X,self.weights))
        #i=0
        #while(i<2):
            #i+=1
        #print(X)
        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias
            #print(y_predicted.shape,y.shape)
            #print(y.shape)-->(80,)

            # compute gradients
            #print(X.shape,y.shape)--> (80,1) (80,)# here, X.shape=(80,1) and y.shape=(80,). so dot product impossible. so, X.T
            #print(np.dot(X.T, (y_predicted - y)))
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y)) #(1/n)*sum(1,n,(2xi*(Y-yi)))
            #print("dw")
            #print(dw)
            db = (1 / n_samples) * np.sum(y_predicted - y) #(1/n)*sum(1,n,(2(Y-yi)))

            # update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        #print(self.weights)--> [75.056427]
        #print(X.shape)-->(20,1)
        y_approximated = np.dot(X, self.weights) + self.bias
        return y_approximated


# Testing
if __name__ == "__main__":
    # Imports
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn import datasets

    def mean_squared_error(y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)

    X, y = datasets.make_regression(
        n_samples=100, n_features=1, noise=20, random_state=4
    )
    #X,y = datasets.make_regression(100,1,20,4)
    #print(X,y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1234
    )

    regressor = LinearRegression(learning_rate=0.01, n_iters=1000)
    regressor.fit(X_train, y_train)
    predictions = regressor.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    #print("MSE:", mse)

    accu = r2_score(y_test, predictions)
    print("Accuracy:", accu)

    y_pred_line = regressor.predict(X)
    cmap = plt.get_cmap("viridis") #get_cmap--> get color map
    fig = plt.figure(figsize=(8, 6))#figsize(float, float), default: rcParams["figure.figsize"] (default: [6.4, 4.8]) Width, height in inches.
    m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
    m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)
    plt.plot(X, y_pred_line, color="black", linewidth=2, label="Prediction")
    plt.show()

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split


class LR:
  def __init__(self,lr=0.05,iter=1000):
    self.lr=lr
    self.iter=iter
    self.weights=None
    self.bias=None
  
  def fit(self,X_train,y_train):
    row,feature=X.shape
    self.weight=np.zeros(feature)
    self.bias=0

    for _ in range(self.iter):
      y_pred=np.dot(X,self.weight)+self.bias
      dw=(1/row)*(np.dot(X.T,(y_pred-y_train)))
      db=(1/row)*(np.sum(y_pred-y_train))
      self.weights-=self.lr*dw
      self.bias=self.lr*db

  def predict(self,X):
    return np.dot(X,self.weight)+self.bias
X,y=datasets.make_regression( n_samples=100, n_features=1, noise=20, random_state=4)

X_train,X_test,y_train,y_test=train_test_split(
        X, y, test_size=0.2, random_state=1234
    )
obj=LR()
obj.fit(X_train,y_train)
print(obj.predict(X_test))