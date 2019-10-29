# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 10:37
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
import csv
users= []
with open('D:\code\python\PageOs\\readfile\data_file\\user_info.csv') as f:
    # 使用字典序列读取，采用列名访问每一列数据
    f_csv = csv.DictReader(f)
    for row in f_csv:
    #     print(row['用户名'])
        users.append(list(row.values()))
print(users)

