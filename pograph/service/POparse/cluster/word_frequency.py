# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 20:22
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
去除停用词
"""
from bs4 import BeautifulSoup
from decimal import Decimal
import re
import nltk
import os
import pandas as pd

# 先将停用词用文件转成列表形式
stop_words=set()
with open('new.txt','r') as f:
    data = f.readlines()
    for line in data:
        stop_words.add(line.strip('\n'))

def cal_body(texts):
    visible_texts = filter(visible, texts)
    result = []
    for text in visible_texts:
        if text != '\n':
            result.append(text)
    total = len(result)
    cfd = nltk.FreqDist(result)
    for key,value in cfd.items():
        value = Decimal(value/total).quantize(Decimal('0.00'))
        cfd[key] = value
    return dict(cfd)

# 返回可见标签中的文本
def visible(element):
    if element.parent.name in ['style', 'script', '[document]','head','title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

# 提取子标签文本的方法
def textual_content(soup,tag_name,list_text):
    for x in soup.find_all(tag_name):
        for child in x.descendants:
            if str(child).startswith('<') or str(child) == '\n':
                pass
            else:
                list_text.append(str(child))
    return list_text

def cal_page(soup):
    # 提取所有<a>中的文本
    a_texts = []
    textual_content(soup,"a", a_texts)
    # 提取所有<title>中的文本
    title_texts = []
    textual_content(soup,"title", title_texts)
    # 提取所有list中<li>-<ol>-<ul>的文本
    li_texts = []
    ol_texts = []
    ul_texts = []
    textual_content(soup,"li", li_texts)
    textual_content(soup,"ol", ol_texts)
    textual_content(soup,"ul", ul_texts)
    lists_texts = list(set(li_texts + ol_texts + ul_texts))
    # 提取所有table中<table>-<tr>-<td>-<th>的文本
    table_texts = []
    tr_texts = []
    td_texts = []
    th_texts = []
    textual_content(soup,"table", table_texts)
    textual_content(soup,"tr", tr_texts)
    textual_content(soup,"td", td_texts)
    textual_content(soup,"th", th_texts)
    tables_texts = list(set(table_texts + tr_texts + td_texts + th_texts))
    # 提取所有heading中<h1>-<h2>-<h3>-<h4>-<h5>-<h6>的文本
    h1_texts = []
    h2_texts = []
    h3_texts = []
    h4_texts = []
    h5_texts = []
    h6_texts = []
    textual_content(soup,"h1", h1_texts)
    textual_content(soup,"h2", h1_texts)
    textual_content(soup,"h3", h1_texts)
    textual_content(soup,"h4", h1_texts)
    textual_content(soup,"h5", h1_texts)
    textual_content(soup,"h6", h1_texts)
    heading_texts = list(set(h1_texts + h2_texts + h3_texts + h4_texts + h5_texts + h6_texts))
    total_texts = list(set(heading_texts + tables_texts + title_texts + lists_texts + a_texts))
    total = len(total_texts)
    for text in total_texts:
        if text in stop_words:
            total_texts=total_texts.remove(text)
    cfd = nltk.FreqDist(total_texts)
    for key, value in cfd.items():
        value = Decimal(value / total).quantize(Decimal('0.00'))
        cfd[key] = str(value)
    return dict(cfd)

def main():
    path = 'D:\code\python\PageOs\POparse\doms'
    files = os.listdir(path)
    dic_WF1 = {}
    dic_WF2 = {}
    print("-------------WF1词频计算开始---------------")
    for file in files:
        html_doc = open(os.path.join(path, file), encoding='UTF-8').read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        texts = soup.findAll(text=True)
        for text in texts:
            if text in stop_words:
                texts.remove(text)
        dic_WF1[file] = cal_body(texts)
    d = pd.DataFrame.from_dict(dic_WF1)
    d.to_csv("wf1.csv")
    print("-------------WF1词频计算结束---------------")
    print("-------------WF2词频计算开始---------------")
    for file in files:
        html_doc = open(os.path.join(path, file), encoding='UTF-8').read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        dic_WF2[file] = cal_page(soup)
    d = pd.DataFrame.from_dict(dic_WF2)
    d.to_csv("wf2.csv")
    print("-------------WF2词频计算结束---------------")
if __name__ == '__main__':
    main()