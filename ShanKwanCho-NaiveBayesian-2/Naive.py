
import pandas as pd
import numpy as np
import math


# implement
def train(df):

    # income data <=50K and >50K
    df1 = df[df['income'] == ' <=50k']
    df2 = df[df['income'] == ' >50k']

    # length of the data
    len1 = len(df1)
    len2 = len(df2)

    # get probability floating num
    prob1 = float(len1) / float(len1+len2)
    prob2 = float(len2) / float(len1+len2)

    # create dictionary
    dictionary = {}
    for col in df1:
        if col != 'income':
            # check keys and values in dictionary for df1
            value_counts1 = df1[col].value_counts()
            dict1 = value_counts1.to_dict()
            for k, v in dict1.items():
                dict1[k] = float(v) / float(len1)

            # check keys and values in dictionary for df1
            value_counts2 = df2[col].value_counts()
            dict2 = value_counts2.to_dict()
            for k, v in dict2.items():
                dict2[k] = float(v) / float(len1)

            #update the dictionary
            dictionary[col] = [dict1, dict2]

    return dictionary, prob1, prob2

# test
def test(df, dictionary, prob1, prob2):

    # empty list
    list = []
    for row in df.iterrow():
        prob_less50 = 1.0
        prob_greater50 = 1.0
        for col in df:
            if row[1][col] in dictionary[col][0][col]:
                prob_less50 *= dictionary[col][0][col][row[1][col]]
            if row[1][col] in dictionary[col][1][col]:
                prob_less50 *= dictionary[col][1][col][row[1][col]]

            prob_less50 *= prob1
            prob_greater50 *= prob2

            if prob2 > prob1:
                list.append(' >50k')
            else:
                list.append(' <=50k')

    return list # predict as list


#main
if __name__ == '__main__':


    # read test and train dataset
    train1 = pd.read_csv('train_replaceData2.csv')
    test1 = pd.read_csv('replaceData_test1.csv')

    # predicted the accuracy passing all the dicts
    dict_, prob1, prob2 = train(train1)
    predictied = test(test1, dict_, prob1, prob2)

    i = 0
    right  = 0
    for item in test1['income'].iterrow():
        if item == predictied[0]:
            right += 1

    accuarcy = float(right) / float(len(df['income']))
    print(accuarcy)
