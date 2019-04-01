# -*- coding: UTF-8 -*-
from __future__ import absolute_import
import unittest

from bok_choy.web_app_test import WebAppTest
from pro_one.litemll_page import LoginPage,UserPage,GoodPage


class Test(WebAppTest):
    def setUp(self):
        super(Test, self).setUp()
        self.login_page = LoginPage(self.browser)
        self.login_page.visit().login("","")
    def test_search(self):
        self.page=UserPage(self.browser)
        search_data=self.page.visit().get_user_data()
        page_dict = {
            'UserPage' : search_data
        }
        for page,params in page_dict.items():
            self.page = eval(page)(self.browser)
            self.page.visit().search(params[0],params[1])


if __name__=='__main__':
    unittest.main()
