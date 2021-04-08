import pandas

def load_data(path,features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient='list')

    new_data = {}
    for i in features:
        new_data[i] = data[i]

    return new_data

def filter_by_feature(data,feature,values):
    data1 = {}
    data2 = {}
    for j in data.keys:
        data1[j] = list
        data2[j] = list

    for i in range(0,len(data[feature])):
        if data[feature][i] in values:
            for n in data.keys:
                data1[n] += data[n][i]

        else:
            for m in data.keys:
                data2[m] += data[m][i]

    return data1, data2

def print_details(data,features,statistic_functions):

    for i in features:
        print(i+': ')
        print(statistic_functions[0](data[i])+', ')
        print(statistic_functions[1](data[i])+', ')
        print(statistic_functions[2](data[i]))


