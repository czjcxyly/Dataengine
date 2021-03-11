# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 15:21:31 2021

@author: yaoluyin
"""

import pandas as pd
from efficient_apriori import apriori
#显示所有列
pd.set_option('max_columns', None)
dataset = pd.read_csv('./Market_Basket_Optimisation.csv',header = None)
#print(dataset)
#print(dataset.shape)#(7501, 20)
transactions=[]
#历遍行
for i in range(0,dataset.shape[0]):
    temp =[]
    for j in range(0,dataset.shape[1]):
        if str(dataset.values[i,j]) != 'nan':
            temp.append(dataset.values[i,j])
    #print(temp)
    transactions.append(temp)

itemset, rules=apriori(transactions,min_support=0.02,min_confidence=0.2)
print('频繁项集：', itemset)
print('关联规则：', rules)