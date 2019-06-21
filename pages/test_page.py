# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 17:31
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/

import unittest
from bok_choy.web_app_test import WebAppTest
from .litemll_page import LoginPage,HomePage,UserPage
class TestLitemall(WebAppTest):
    def setUp(self):
        super(TestLitemall,self).setUp()
        self.login_page = LoginPage(self.browser)
        self.login_page.visit().login("admin123","admin123")
    def test_add_user(self):
        """测试添加用户"""
        self.home_page = HomePage(self.browser)
        self.user_page = UserPage(self.browser)
        self.home_page.goto_user()
        self.user_page.add_user("zhengjiani","11111111")
        results = self.list_page_search_user("zhengjiani","11111111")
        assert "zhengjiani" in results