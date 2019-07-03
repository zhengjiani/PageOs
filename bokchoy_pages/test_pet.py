# -*- coding: utf-8 -*-
# @Time    : 2019/6/9 8:57
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
import os
import unittest
from bok_choy.web_app_test import WebAppTest
from .pet_page import HomePage,FindPage
class TestPet(WebAppTest):
    def setUp(self):
        super(TestPet,self).setUp()
    def test_find_owner(self):
        self.home_page = HomePage(self.browser)
        self.home_page.visit()
        self.find_page = FindPage(self.browser)
        self.find_page.find_owner('hengjian')
if __name__ == '__main__':
    os.environ['SELENIUM_BROWSER'] = 'Chrome'
    unittest.main()