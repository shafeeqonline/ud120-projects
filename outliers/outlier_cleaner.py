#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    my_list = []
    for x in range(0, len(predictions)):
        diff = float(net_worths[x] - predictions[x]) * float(net_worths[x] - predictions[x])
        my_list.append(diff)
    my_list.sort()
    tresholdDiff = my_list[80]
    # print predictions
    cleaned_data = []
    print tresholdDiff
    for x in range(0, len(predictions)):
        diff_new = float(net_worths[x] - predictions[x]) * float(net_worths[x] - predictions[x])
        if diff_new <= tresholdDiff:
            # print "yes", ages[x]
            cleaned_data.append((ages[x], net_worths[x], diff_new))
    # print cleaned_data
    ### your code goes here

    
    return cleaned_data

