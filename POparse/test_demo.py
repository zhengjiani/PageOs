# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 13:30
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'html.parser')
# 按照标准缩进格式输出
# print(soup.prettify())
# 简单的浏览结构化数据
print(soup.title)
# <title>The Dormouse's story</title>
print(soup.title.name)
# title
print(soup.title.string)
# The Dormouse's story
print(soup.title.parent.name)
# head
print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>
print(soup.p['class'])
# title
print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# 一般是第一个链接
print(soup.find_all('a'))
# 打印所有链接，并放入列表
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print(soup.find(id="link3"))
# 用id找链接
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# 从文档中找到所有<a>标签的链接
for link in soup.find_all('a'):
    print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie
# 从文档中获取所有文字内容
print(soup.get_text())
# 子孙节点遍历
head_tag = soup.head
for child in head_tag.descendants:
    print(child)
    # <title>The Dormouse's story</title>
    # The Dormouse's story