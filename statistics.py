def sum(values):
    sum = 0
    for i in values:
        sum += i

    return sum

def mean(values):
    sum = 0
    for i in values:
        sum += i

    mean = sum/len(values)
    return mean

def median(values):
    med = 0
    values.sort()
    n = len(values)
    if n%2:
        med = values[(n+1)/2]
    else:
        med = (values[n/2] + values[(n+1)/2])/2

    return med

def population_statistics(feature_description, data, treatment, target, threshold, is_above,
statistic_functions):

