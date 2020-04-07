#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
sys.path.append("../tools/")
from time import time
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#features_train = features_train[:round(len(features_train)/100)]
#labels_train = labels_train[:round(len(labels_train)/100)]

clf= SVC(kernel="rbf", C=10000)
t0 = time()
clf.fit(features_train,labels_train) 
print("train time:")
print(time()-t0)

t0 = time()
y_pred=clf.predict(features_test) 
print("test time:")
print(time()-t0)

accuracy=accuracy_score(y_pred,labels_test)
print('Accuracy: {}'.format(accuracy))

#########################################################


