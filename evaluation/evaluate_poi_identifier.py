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
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
import sklearn.metrics as metrics
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

X = features
y = labels

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=42)

dt = DecisionTreeClassifier()
dt.fit(X=train_X, y=train_y)
predict_y =dt.predict(X=test_X)
print "POI in test:", len([poi for poi in test_y if poi==1])
print "Total in test:", len(test_y)
print "True positives:", [(o,i) for o,i in zip(test_y, predict_y) if o==i==1]
print "Precision:", metrics.precision_score(y_true=test_y, y_pred=predict_y)
print "Recall:", metrics.recall_score(y_true=test_y, y_pred=predict_y)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print "Confusion report for arrays:\n", metrics.classification_report(true_labels, predictions)
print "Confusion matrix for arrays:\n", metrics.confusion_matrix(true_labels, predictions)


