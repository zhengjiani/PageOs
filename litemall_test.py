# -*- encoding: utf-8 -*-
"""
@File    : litemall_test.py
@Time    : 2019/11/4 2:47 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from selenium import webdriver
from litemall_page import SearchPage
import unittest
class LitemallTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:9527/')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/form/button').click()
    def tearDown(self):
        self.driver.close()
    def test_search(self):
        self.search_page = SearchPage(self.driver)
        self.search_page.type_username('user123')
        self.search_page.type_phone('13319088282')
        self.search_page.search()
if __name__ == '__main__':
    unittest.main()