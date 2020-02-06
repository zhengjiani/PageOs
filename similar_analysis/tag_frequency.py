# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 11:09
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from bs4 import BeautifulSoup
from decimal import Decimal
import os
import pandas as pd


# html_doc = open('D:\code\python\PageOs\similar_analysis\cluster\index.html').read()



def tag_frequency(soup, tag_name, tag_total):
    tag_name_list = soup.find_all(tag_name)
    tag_tf = Decimal(len(tag_name_list) / tag_total).quantize(Decimal('0.00'))
    return tag_tf

def tag_numbers(soup, tag_name):
    tag_name_list = soup.find_all(tag_name)
    tag_num = len(tag_name_list)
    return tag_num

def cal_tagtf(tag_lists, soup, tag_total):
    tags = set()
    for tag in tag_lists:
        if tag.name is not None:
            tags.add(tag.name)
    tags_tf = {}
    for i in tags:
        tags_tf[i] = str(tag_frequency(soup, i, tag_total))
    return tags_tf

def cal_tagtn(tag_lists, soup):
    tags = set()
    for tag in tag_lists:
        if tag.name is not None:
            tags.add(tag.name)
    tags_tf = {}
    for i in tags:
        tags_tf[i] = str(tag_numbers(soup, i))
    return tags_tf


def main():
    base_dir = os.path.dirname(__file__)
    dom_dir = os.path.join(base_dir, 'doms')
    files = os.listdir(dom_dir)
    dic = {}
    for file in files:
        # if os.path.splitext(file)[1] == '.html':
        # 采用绝对路径os.path.join()
        html_doc = open(os.path.join(dom_dir, file), encoding="unicode_escape").read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        # 获取网页中所有标签并存入列表中
        tag_lists = list(soup.descendants)
        tag_total = len(tag_lists)
        # dic[file] = cal_tagtf(tag_lists, soup, tag_total)
        dic[file] = cal_tagtn(tag_lists, soup)
    # print(dic)
    d = pd.DataFrame.from_dict(dic)
    print(d)
    # 矩阵转置
    d1 = pd.DataFrame(d.values.T, index=d.columns, columns=d.index)
    # print(d1)
    # d.to_csv("tf.csv")
    d1.to_csv("tn.csv")

if __name__ == '__main__':
    main()
