# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 16:58
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from bs4 import BeautifulSoup

url = 'D:\code\python\PageOs\DOMparse\source.html'
soup = BeautifulSoup(open(url,'r',encoding = 'utf-8'),features="lxml")
print(soup.title)
print(soup.div)