# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 13:29
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from bs4 import BeautifulSoup
from jinja2 import Template
from jinja2 import Environment,PackageLoader

env = Environment(loader=PackageLoader('POparse'))
template = env.get_template('locators.j2')
html_doc = open('D:\code\python\PageOs\POparse\doms\index.html').read()

soup = BeautifulSoup(html_doc,'html.parser')
# print(soup.select("a[href]"))
# print(soup.select("a[title]"))
dic_link = {}
for a_tag in soup.find_all("a"):
    for span in a_tag.find_all("span"):
        if span.string is not None:
            # print(a_tag.get("href"),span.string)
            dic_link[a_tag.get("href")]=span.string
print(dic_link)
for value in dic_link.values():
    dic={
        'loc_name':value.upper(),
        'link_name':value
    }
    content = template.render(dic)
    print(content)
