# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 15:40
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""利用poium"""
from poium import Page,PageElement

class BaiduPage(Page):
    """百度Page层，百度页面封装操作的元素"""
    search_input = PageElement(id_="kw")
    search_button = PageElement(id_="su")