# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 11:12
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
# 从result.json中获取每个页面的URL
"""计算URL的字符串编辑距离"""
import json
import Levenshtein
import pandas as pd
def cal_levenshteinDistance(data):
    url_dic = {}
    for state1 in data['states']:
        # 除去URL中的参数，如?、&等<--没有实现，后面实现-->
        url_dic[state1] = {}
        for state2 in data['states']:
            url1 = data['states'][state1]['url']
            url2 = data['states'][state2]['url']
            l = Levenshtein.ratio(url1, url2)
            # l1=Levenshtein.distance(url1,url2)
            # print(state1, state2)
            # print(format(l,'.2f'))
            url_dic[state1][state2] = format(l, '.2f')
    return url_dic

# print(data)
# URL总数，即去除重复后的URL
# for url,state in data['statistics']["stateStats"]["urls"].items():
#     print(url,state)
def main():
    with open('D:\code\python\PageOs\POparse\\result.json', 'r') as f:
        data = json.load(f)
    url_dic=cal_levenshteinDistance(data)
    d=pd.DataFrame.from_dict(url_dic)
    print(d)
    d.to_csv("url.csv")




