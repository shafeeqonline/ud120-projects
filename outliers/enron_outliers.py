#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL', 0);
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

max_salary = 0
for point in data:
    salary = point[0]
    bonus = point[1]
    if max_salary < salary:
        max_salary = salary
    matplotlib.pyplot.scatter( salary, bonus )

print max_salary
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


### your code below



