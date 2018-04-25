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
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 



a_train, a_test, b_train, b_test = train_test_split(features, labels, test_size=0.3, random_state=42)


clf = DecisionTreeClassifier(random_state=0)
clf.fit(a_train, b_train)
pred = clf.predict(a_test)

print "pred", "label"
for x in range(0, len(pred)):
    print pred[x], b_test[x]
print(clf.score(a_test, b_test))

print "precision_score", precision_score(b_test, pred)
print "recall_score", recall_score(b_test, pred)

total_poi_in_test = 0
for x in b_test:
    if float(x) == 1.0:
        total_poi_in_test += 1

print total_poi_in_test, "total_poi_in_test"
print "total people in test set", len(b_test)
