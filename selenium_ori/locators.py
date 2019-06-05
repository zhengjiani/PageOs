# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 16:47
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
其中一种做法是将定位器字符串与它们被使用的位置分开。 在此示例中，同一页面的定位器属于同一个类。
有种策略模式的感觉
"""
from selenium.webdriver.common.by import By
class MainPageLocators(object):
    """所有主页的定位器都应该放在这里"""
    GO_BUTTON = (By.ID,'submit')

class SearchResultsPageLocators(object):
    """所有搜索结果的定位器都应该放在这里"""
    pass