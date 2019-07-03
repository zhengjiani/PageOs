# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 22:32
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from bs4 import BeautifulSoup
import nltk
from decimal import Decimal
html_doc = open('D:\code\python\PageOs\POparse\doms\index.html')
soup = BeautifulSoup(html_doc, 'html.parser')
# 提取子标签文本的方法
def textual_content(tag_name,list_text):
    for x in soup.find_all(tag_name):
        for child in x.descendants:
            if str(child).startswith('<') or str(child) == '\n':
                pass
            else:
                list_text.append(str(child))
    return list_text

# 提取所有<a>中的文本
a_texts=[]
textual_content("a",a_texts)
# 提取所有<title>中的文本
title_texts = []
textual_content("title",title_texts)
# 提取所有list中<li>-<ol>-<ul>的文本
li_texts = []
ol_texts = []
ul_texts = []
textual_content("li",li_texts)
textual_content("ol",ol_texts)
textual_content("ul",ul_texts)
lists_texts=li_texts+ol_texts+ul_texts
print(list(set(lists_texts)))
# 提取所有table中<table>-<tr>-<td>-<th>的文本
table_texts = []
tr_texts = []
td_texts = []
th_texts = []
textual_content("table",table_texts)
textual_content("tr",tr_texts)
textual_content("td",td_texts)
textual_content("th",th_texts)
tables_texts=table_texts+tr_texts+td_texts+th_texts
print(list(set(tables_texts)))
# 提取所有heading中<h1>-<h2>-<h3>-<h4>-<h5>-<h6>的文本
h1_texts = []
h2_texts = []
h3_texts = []
h4_texts = []
h5_texts = []
h6_texts = []
textual_content("h1",h1_texts)
textual_content("h2",h1_texts)
textual_content("h3",h1_texts)
textual_content("h4",h1_texts)
textual_content("h5",h1_texts)
textual_content("h6",h1_texts)
heading_texts=h1_texts+h2_texts+h3_texts+h4_texts+h5_texts+h6_texts
print(list(set(heading_texts)))
total_texts = list(set(heading_texts+tables_texts+title_texts+lists_texts+a_texts))
total = len(total_texts)
cfd = nltk.FreqDist(total_texts)
for key, value in cfd.items():
    value = Decimal(value / total).quantize(Decimal('0.00'))
    cfd[key] = str(value)
print(dict(cfd))