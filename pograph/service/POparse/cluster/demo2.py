# -*- encoding: utf-8 -*-
"""
@File    : demo2.py
@Time    : 2019/11/9 12:15 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
close_part = None
closet_part = (1,2)
part1,part2 = closet_part
print(part1)
print(part2)

# 获取目录下文件数目
import os
path = '/Users/zhengjiani/PycharmProjects/PageOs_latest/pograph/service/POparse/doms'
print('filenum:',len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))]))

