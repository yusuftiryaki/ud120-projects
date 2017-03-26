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
import sys
import pickle


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print enron_data.items()[0]
print "# of Data:",len(enron_data)
print "# of Features:",len(enron_data.values()[0])
num_poi = 0
for row in enron_data.items():
    if row[1]["poi"] == True:
        num_poi = num_poi+1

print "# of POI:",num_poi


print "James Prentice Stock:", enron_data["Prentice James".upper()]["total_stock_value"]

print "Wesley Colwell email to poi:", enron_data["Colwell Wesley".upper()]["from_this_person_to_poi"]

print "Jeffrey K Skilling exercised stock:", enron_data["Skilling Jeffrey K".upper()]["exercised_stock_options"]

print "Qt Salary:",[key for key,val in enron_data.items() if val["salary"] != "NaN"].__len__()
print "Known Email:",[key for key,val in enron_data.items() if val["email_address"] != "NaN"].__len__()
num_total_pay = [key for key,val in enron_data.items() if val["total_payments"] == "NaN"].__len__()
num_total_pay_poi = [key for key,val in enron_data.items() if val["total_payments"] == "NaN" and val["poi"]==True].__len__()
print "Qt Payment:{} Percent:{}".format(num_total_pay,float(num_total_pay)/len(enron_data))
print "Qt Payment POI:{} Percent:{}".format(num_total_pay_poi,float(num_total_pay_poi)/len(enron_data))



