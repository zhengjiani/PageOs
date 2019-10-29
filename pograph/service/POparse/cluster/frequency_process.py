# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 18:44
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from collections import defaultdict
import pandas as pd
# 比较字典大小模块
import operator
def tag_process(cols,df,i):
    """

    :param cols: .csv文件中所有列名 i:cols的有效索引下标位置
    :return:
    """
    # 合并tag_frequency相等的行
    dic = {}
    res1 = {}
    dct = defaultdict(list)
    func = lambda z: dict([(x, y) for y, x in z.items()])
    for page in cols[i:]:
        dic[page] = df.groupby(page).groups
    for k,v in dic.items():
        for key,value in v.items():
            dic[k][key] = list(value)
    for k1,v1 in dic.items():
        for k2,v2 in dic.items():
            if operator.eq(v1,v2):
                dct[k1].append(k2)
                res1[k2] = k1
    return set(func(func(res1)))
    # 验证时使用
    # return dct
if __name__ == "__main__":
    # 合并以“tag_frequency”为标准的相同页面
    csv_file = ["tf.csv","wf1.csv","wf2.csv"]
    for file in csv_file:
        cols = list(pd.read_csv(file, nrows=1))
        df = pd.read_csv(file, usecols=[i for i in cols if i != 'alchemyGraph.json'])
        print(file,tag_process(cols,df,2))

    csv2_file = ["url.csv", "dom_string.csv"]
    for file in csv2_file:
        cols = list(pd.read_csv(file, nrows=1))
        df = pd.read_csv(file)
        print(file, tag_process(cols, df, 1))

