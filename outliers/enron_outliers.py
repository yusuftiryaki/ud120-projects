#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
import numpy as np
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
#del data_dict["TOTAL"]
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
salary = data[:, 0:1]
bonus = data[:, 1:2]
reg.fit(salary, bonus)
plt.scatter(x=salary, y=bonus)
plt.plot(salary, reg.predict(salary), color="red" )
plt.show()

errors = abs(salary - reg.predict(salary))
outliers = zip(salary, errors)
for i in range(5):
    max_error = max(outliers, key=lambda x: x[1])
    outliers.remove(max_error)
    for key,val in data_dict.items():
        if val["salary"] == max_error[0][0]:
            print key




