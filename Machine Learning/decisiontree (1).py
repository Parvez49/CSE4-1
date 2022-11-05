# -*- coding: utf-8 -*-
"""DecisionTree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QnSYNtxxSY26igbDp5-DeTj3SpvfGusF
"""

import numpy as np

def entropy(y):
    hist=np.bincount(y)
    sum=0
    for h in hist:
        p=h/len(y)
        sum=sum-np.log2(p)*p
    return sum
def InformationGain(Y,left_index,right_index):
    left_ent = entropy(Y[left_index])
    right_ent = entropy(Y[right_index])
    return entropy(Y) - len(left_index) / len(Y) * left_ent - len(right_index) / len(Y) * right_ent

X=np.array([[1,30],[1,15],[1,5],[0,10],[0,5],[0,15],[0,20],[0,25],[0,30],[0,30]])
Y=np.array([0,0,0,0,0,1,1,1,1,1])

n_feature=X.shape[1]
for i in range(0,n_feature):
    print("for feature: " + str(i))
    X_column=X[:,1]
    #print(X_column)
    thresholds=np.unique(X_column)
    #print("thresholds",thresholds)
    for threshold in thresholds:
        left_index=np.argwhere(X_column<=threshold).flatten()
        right_index=np.argwhere(X_column>threshold).flatten()
        #print(left_index,right_index)
        IG=InformationGain(Y,left_index,right_index)
        print(IG)



"""
input=[[1,30,'no'],
       [1,15,'no'],
       [1,5,'no'],
       [0,10,'no'],
       [0,5,'no'],
       [0,15,'yes'],
       [0,20,'yes'],
       [0,25,'yes'],
       [0,30,'yes'],
       [0,30,'yes']]


def Entropy(list):
    n=0
    y=0
    for i in range(len(input)):
        if input[i][2]=='no':
            n+=1
        else: y+=1


ent=Entropy(input)


"""