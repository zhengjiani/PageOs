# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 11:09
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from bs4 import BeautifulSoup
from decimal import Decimal
import os
import pandas as pd
# html_doc = open('D:\code\python\PageOs\POparse\cluster\index.html').read()
def read_file():
    pass

def tagFrequency(soup,tag_name,tag_total):
    tag_name_list = soup.find_all(tag_name)
    tag_tf = Decimal(len(tag_name_list)/tag_total).quantize(Decimal('0.00'))
    return tag_tf

def cal_tagtf(tag_lists,soup,tag_total):
    tags = set()
    for tag in tag_lists:
        if tag.name is not None:
            tags.add(tag.name)
    tags_tf = {}
    for i in tags:
        tags_tf[i] = str(tagFrequency(soup,i,tag_total))
    return tags_tf
def main():
    path = 'D:\code\python\PageOs\POparse\doms'
    files = os.listdir(path)
    dic = {}
    for file in files:
        # if os.path.splitext(file)[1] == '.html':
        # 采用绝对路径os.path.join()
        html_doc = open(os.path.join(path,file),encoding='UTF-8').read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        # 获取网页中所有标签并存入列表中
        tag_lists = list(soup.descendants)
        tag_total = len(tag_lists)
        dic[file] = cal_tagtf(tag_lists,soup,tag_total)
    # print(dic)
    d=pd.DataFrame.from_dict(dic)
    print(d)
    d.to_csv("tf.csv")
if __name__ == '__main__':
    main()