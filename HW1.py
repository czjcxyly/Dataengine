from pandas import Series, DataFrame
data = {'Chinese': [68, 95, 98, 90,80], 'Math': [65, 76, 86, 88, 90], 'English': [30, 98, 88, 88, 90]}
df1 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], columns=['Chinese', 'Math', 'English'])
print(df1)
print("语文,平均成绩：",df1['Chinese'].mean(),"，最低成绩：",df1['Chinese'].min(),"，最高成绩：",df1['Chinese'].max(),"，方差：",df1['Chinese'].var(),"，标准差：",df1['Chinese'].std(),"。")
print("数学,平均成绩：",df1['Math'].mean(),"，最低成绩：",df1['Math'].min(),"，最高成绩：",df1['Math'].max(),"，方差：",df1['Math'].var(),"，标准差：",df1['Math'].std(),"。")
print("英语,平均成绩：",df1['English'].mean(),"，最低成绩：",df1['English'].min(),"，最高成绩：",df1['English'].max(),"，方差：",df1['English'].var(),"，标准差：",df1['English'].std(),"。")
df1['Sum']=df1.apply(lambda x:x.sum(),axis=1)
print("总成绩排名：")
print(df1.sort_values(by='Sum', ascending=False))