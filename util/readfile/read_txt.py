# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 10:26
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
#读取文件
with(open("D:\code\python\PageOs\\readfile\data_file\\user_info")) as user_file:
    data = user_file.readlines()
#格式化处理
users = []
for line in data:
    user = line[:-1].split(":")
    users.append(user)
#打印users二维数组
print(users)