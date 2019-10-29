# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 8:47
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
import os
os.chdir("D:\\code\\python\\PageOs")
r=os.popen('java -jar RTED_v1.2.jar -t {a{b}{c}} {a{b{d}}} -o -v')
str1=r.readlines()[0]
print(str1.split(' ')[-1])

