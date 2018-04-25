#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print len(enron_data[list(enron_data)[0]])
# print enron_data[list(enron_data)[0]]['poi']


poiCount = 0
quantifiedSalary = 0
knownEmailAddress = 0
for x in range(0, len(enron_data)):
    if enron_data[list(enron_data)[x]]['poi']:
        poiCount = poiCount + 1
    if math.isnan(float(enron_data[list(enron_data)[x]]['total_payments'])) and enron_data[list(enron_data)[x]]['poi']:
        quantifiedSalary = quantifiedSalary + 1
    if enron_data[list(enron_data)[x]]['email_address'] != 'NaN':
        knownEmailAddress = knownEmailAddress + 1

print quantifiedSalary, len(enron_data)
print "percentage", float(quantifiedSalary * len(enron_data) / 100)

# print "dsfsd", enron_data[list(enron_data)[100]]['salary']
# print len(enron_data)
# for x in range(0, len(enron_data)):
    # print (enron_data[list(enron_data)[x]]['email_address'])
    

print poiCount

# print enron_data['PRENTICE JAMES']
# print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
# print enron_data['SKILLING JEFFREY K']['exercised_stock_options']
# print enron_data['LAY KENNETH L']

# print quantifiedSalary
print quantifiedSalary
print knownEmailAddress