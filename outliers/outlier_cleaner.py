#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    #make the list of tuples with the error
    for i in range(len(ages)):
        error=predictions[i]-net_worths[i]
        cleaned_data.append((ages[i],net_worths[i],error))
    
    #sort list of truples by the 3th element of each tuple
    cleaned_data.sort(key=lambda tup: tup[2])
    
    #select 90% of the first tuples
    ndrop=round(0.9*len(ages))
    cleaned_data=cleaned_data[:ndrop]
    
    return cleaned_data

