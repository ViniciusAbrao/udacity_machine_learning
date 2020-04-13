#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, \
    confusion_matrix, f1_score 
                                

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf= DecisionTreeClassifier()
clf.fit(features_train,labels_train) 
y_pred=clf.predict(features_test) 

accuracy=accuracy_score(labels_test,y_pred)
print('Accuracy: {}'.format(accuracy))

precision=precision_score(labels_test,y_pred)
print('Precision: {}'.format(precision))

recall=recall_score(labels_test,y_pred)
print('Recall: {}'.format(recall))

matrix=confusion_matrix(labels_test,y_pred)
print('Matrix: {}'.format(matrix))

f1=f1_score(labels_test,y_pred)
print('f1: {}'.format(f1))
