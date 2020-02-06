# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 18:44
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
import pandas as pd
# 比较字典大小模块
import operator
cols = list(pd.read_csv("csv_file/tf.csv", nrows=1))
df = pd.read_csv("csv_file/tf.csv", usecols=[i for i in cols if i != 'alchemyGraph.json'])
dic = {}
for page in cols[2:]:
    dic[page] = df.groupby(page).groups
for k,v in dic.items():
    for key,value in v.items():
        dic[k][key] = list(value)
res = {}
res1 = {}
for k1,v1 in dic.items():
    res[k1] = []
    for k2,v2 in dic.items():
        if operator.eq(v1,v2):
            res[k1].append(k2)
            res1[k2] = k1
func = lambda z:dict([(x, y) for y, x in z.items()])
print(set(func(func(res1))))
