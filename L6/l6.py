# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 19:27:40 2021

@author: Lewis
"""
import pandas as pd
from fbprophet import Prophet
#导入数据
train = pd.read_csv('./train.csv')
#print(train)
train['Datetime'] = pd.to_datetime (train['Datetime'])
#print(train)
train.index = train['Datetime']
train.drop(['ID','Datetime'], axis=1, inplace=True)
#print(train)
#数据处理
daily_train = train.resample('D').sum()
#print(daily_train)
daily_train['ds'] = daily_train.index
daily_train['y'] = daily_train['Count']
daily_train.drop(['Count'], axis=1, inplace=True)
#print(daily_train)
#预测
m = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.1)
m.fit(daily_train)
future = m.make_future_dataframe(periods=213)
#print(future)
forecast = m.predict(future)
m.plot(forecast)