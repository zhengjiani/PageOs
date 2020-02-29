# -*- coding: utf-8 -*-
import os
import unittest
from bok_choy.web_app_test import WebAppTest
from bokchoy_pages.pet_page import *
class TestPet(WebAppTest):
    def setUp(self):
        super(TestPet, self).setUp()

    def test_add_Owner(self):
        """测试添加主人"""
        self.home_page = HomePage(self.browser)
        self.home_page.goto_register()
        self.regist_page = RegisterPage(self.browser)
        self.regist_page.visit()

        self.regist_page.regist_owner("zjn","zjn","xian","xiann","123")
if __name__ == '__main__':

    unittest.main()