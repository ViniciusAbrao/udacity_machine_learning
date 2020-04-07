""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
sys.path.append("../tools/")
from time import time
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

clf= GaussianNB()
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


