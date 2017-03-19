#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
#########################################################
small_dataset = False
if small_dataset:
    features_train = features_train[:len(features_train)/100]
    labels_train = labels_train[:len(labels_train)/100]

svcs = [SVC(kernel="rbf",C=10),SVC(kernel="rbf",C=100),SVC(kernel="rbf",C=1000),SVC(kernel="rbf",C=10000)]
svcs = [SVC(kernel="rbf",C=10000)]
for svc in svcs:
    t0 = time()
    svc.fit(features_train, labels_train)
    print "training time:",svc.__getattribute__("C"), round(time() - t0, 3), "s"
    t0 = time()
    predict = svc.predict(features_test)
    print "predicting time:", round(time() - t0, 3), "s"
    print accuracy_score(y_true=labels_test, y_pred=predict)
    print "10th:",predict[10],"26th:",predict[26],"50th:",predict[50]
    print "num Chris:",len([chris for chris in predict if chris==1])




