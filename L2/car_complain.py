# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:35:22 2021

@author: yaoluyin
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
#创建函数
def get_page_content(request_url):
    # 得到页面的内容
    #print(request_url)
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(request_url,headers=headers,timeout=20)
    content = html.text
    # 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser')
    return soup
#分析当前页面的投诉信息
def analysis(soup):
    temp = soup.find('div', class_="tslb_b")
    #创建DataFrame
    df = pd.DataFrame(columns=['id','brand','car_model','type','desc','problem','datetime','status'])
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        #提取汽车投诉信息
        temp={}
        td_list = tr.find_all('td')
        if len(td_list)>0:
            #解析各个字段内容
            id,brand,car_model,type,desc,problem,datetime,status = td_list[0].text, td_list[1].text,td_list[2].text,td_list[3].text,td_list[4].text,td_list[5].text,td_list[6].text,td_list[7].text
            #放到dataFrame中
            temp['id'], temp['brand'], temp['car_model'], temp['type'], temp['desc'], temp['problem'], temp['datetime'], temp['status'] = id,brand,car_model,type,desc,problem,datetime,status
            df = df.append(temp, ignore_index=True)
    return df

result=pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datatime', 'status'])
# 请求URL
base_url='http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
page_num=3
for i in range(page_num):
    #拼接url
    request_url=base_url+str(i+1)+'.shtml'
    #得到soup解析
    soup=get_page_content(request_url)
    #得到当前页面的dataframe
    df=analysis(soup)
    #print(df)
    result=result.append(df)
print(result)
result.to_excel('car_compain1.xlsx',index=False)

