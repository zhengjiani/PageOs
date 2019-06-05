# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 14:44
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get("https://github.com/zhengjiani?tab=repositories")
elems = driver.find_element_by_id("user-repositories-list")
elem=elems.find_elements_by_tag_name("a")
repos = []
for i in range(len(elem)):
    repos.append(elem[i].text)
repos = [elem for elem in repos if elem != "1"]
print(repos)
driver.close()
