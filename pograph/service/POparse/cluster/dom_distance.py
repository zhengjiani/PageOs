# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 15:15
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
将去除文本后的DOM转化为字符串，比较距离DOM-RTED and DOM-Lev
"""
import os
import re
import Levenshtein
import pandas as pd
from bs4 import BeautifulSoup

class DOMString:
    def remove_tag_content(self,soup,tag_name):
        """
        :param tag_name: string
        :return: soup
        """
        for tag in soup.find_all(tag_name):
            tag.clear()
    def remove_all_tags(self,soup):
        self.remove_tag_content(soup, "a")
        self.remove_tag_content(soup, "title")
        self.remove_tag_content(soup, "h2")
        self.remove_tag_content(soup, "li")
        self.remove_tag_content(soup, "span")
        self.remove_tag_content(soup, "button")
        return soup
    def get_domdict(self):
        # 去除DOM中所有的文本
        path = '/Users/zhengjiani/PycharmProjects/PageOs_latest/pograph/service/POparse/doms'
        files = os.listdir(path)
        dic_DOMLev = {}
        print("-------------DOMLev计算开始---------------")
        for file1 in files:
            html_doc1 = open(os.path.join(path, file1), encoding='UTF-8').read()
            soup = BeautifulSoup(html_doc1, 'html.parser')
            result_dom1 = self.remove_all_tags(soup)
            string_dom1 = str(result_dom1).replace('\n', '')
            dic_DOMLev[file1] = {}
            for file2 in files:
                html_doc2 = open(os.path.join(path, file2), encoding='UTF-8').read()
                soup = BeautifulSoup(html_doc2, 'html.parser')
                result_dom2 = self.remove_all_tags(soup)
                string_dom2 = str(result_dom2).replace('\n', '')
                l = Levenshtein.ratio(string_dom1, string_dom2)
                # n=Levenshtein.
                dic_DOMLev[file1][file2] = format(l, '.2f')
        return dic_DOMLev
        # d = pd.DataFrame.from_dict(dic_DOMLev)
        # # print(d)
        # d.to_csv("dom_string.csv")
        print("-------------DOMLev计算结束---------------")
if __name__ == '__main__':
    d = DOMString()
    print(d.get_domdict())