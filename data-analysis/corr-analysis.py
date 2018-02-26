# coding: utf-8

import pandas as pd
#数据日期为2018-02-23开始降序排列，pandas会按照索引对应每条数据
emotions = pd.read_csv('emotions-reverse.csv',header=None)#余额宝情绪指数
index = pd.read_csv('000001-clip.csv')#上证指数

print emotions.head()
print index.head()

d3 = index.iloc[:, 3]

d2 = emotions.iloc[:, 1]
# 两列的相关系数
corr = d2.corr(d3)
print u'相关系数:', corr, '--->',
if (abs(corr) >= 0.8):
    print u'高度相关'
elif (abs(corr) >= 0.3):
    print u'中度相关'
else:
    print u'低度相关'