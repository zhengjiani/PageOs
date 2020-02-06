# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 19:54
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
去除文本文件中的空行
stopwords.txt去空行前的文件，new.txt去空行后的文件
f为处理前文件所在文件夹，f_new为处理后文件所在文件夹
"""
import os

base_dir = os.path.dirname(__file__)
# print(base_dir)
# 获取文件拼接后路径
path = os.path.join(base_dir, 'doms/index.html')
# print(path)
f = open(path)
f_new = open(os.path.join(base_dir, 'new_index.html'), 'w')
for line in f.readlines():
    data = line.strip()
    if len(data) != 0:
        print(data)
        f_new.write(data)
        f_new.write('\n')
f.close()
f_new.close()
