#!/usr/bin/python
import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    outlier_count = int(len(ages)*0.1)
    cleaned_data = zip(ages,net_worths,abs(net_worths - predictions))

    for i in range(outlier_count):
        cleaned_data.remove(max(cleaned_data, key=lambda x : x[2]))

    print "%i items removed as outlier" % outlier_count
    return cleaned_data
