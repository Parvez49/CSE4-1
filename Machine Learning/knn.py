# -*- coding: utf-8 -*-
"""KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qBqtD_bfvJhVJQNEz4-Gb-4qXlLJu1nn
"""

from collections import Counter

import numpy as np


def euclidean_distance(x1, x2):
    #print("x1, x2",x1,x2)
    #print(np.sqrt(np.sum((x1 - x2) ** 2)))
    return np.sqrt(np.sum((x1 - x2) ** 2))


class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        #print(X,y)
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        #print(y_pred)
        return np.array(y_pred)

    def _predict(self, x):
        #print("predict")
        #print(x)
        # Compute distances between x and all examples in the training set
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        #print(distances)
        # Sort by distance and return indices of the first k neighbors
        #print(np.argsort(distances))
        k_idx = np.argsort(distances)[: self.k]
        #print("k_idx",k_idx)
        # Extract the labels of the k nearest neighbor training samples
        k_neighbor_labels = [self.y_train[i] for i in k_idx]
        #print(k_neighbor_labels)
        # return the most common class label
        most_common = Counter(k_neighbor_labels).most_common(1) # [('0', 5), ('1', 4), ('2', 3)]
        #print(most_common)
        return most_common[0][0]


if __name__ == "__main__":
    # Imports
    from matplotlib.colors import ListedColormap
    from sklearn import datasets
    from sklearn.model_selection import train_test_split

    cmap = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])

    def accuracy(y_true, y_pred):

        #print(y_true, y_pred)
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy

    iris = datasets.load_iris()
    #print(iris)
    X, y = iris.data, iris.target

    #print(X)
    #print()
    #print(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1234
    )

    #print(y_train)
    k = 3
    clf = KNN(k=k)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    print("KNN classification accuracy", accuracy(y_test, predictions))

from collections import Counter
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split


def dist(i,x):
  return np.sqrt(np.sum(i-x)**2)

def accuracy(y_test,y_pred):
  return np.sum(y_test==y_pred)/len(y_test)


class KNN2:
  def __init__(self,k):
    self.k=k
  def fit(self,X_train,y_train):
    self.X_train=X_train
    self.y_train=y_train
  def predict(self,X_test):
    y_pred=[self._pred(i) for i in X_test]
    return y_pred
  def _pred(i):
    distances=[dist(i,x) for x in self.X_train]
    sortdist=np.argsort(distances)[:self.k]

    y_value=[self.y_test(i) for i in sortdist]

    count=Counter(y_value).most_common(1)
    return count[0][0]


iris=datasets.load_iris()
#print(iris)
X,y=iris.data,iris.target
#print(X,y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=1234)
k=3
clf=KNN(k=k)
clf.fit(X_train,y_train)
pred=clf.predict(X_test)
print(accuracy(y_test,pred))