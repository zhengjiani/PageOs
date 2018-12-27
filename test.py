# -*- coding: UTF-8 -*-
from __future__ import absolute_import
import os
import time
import unittest
from bok_choy.promise import BrokenPromise
from ddt import ddt,data,unpack
from bok_choy.web_app_test import WebAppTest
from tests.demo.page import LoginPage,HomePage,UserPage,ResultUserPage
class Test(WebAppTest):
    def setUp(self):
        '''
        Instantiate the page object.
        :return:
        '''
        super(Test,self).setUp()
        self.login_page=LoginPage(self.browser)
        self.login_page.visit().login('','')
    # def test_link(self):
    #     self.page=HomePage(self.browser)
    #     self.page.jump('用户管理')
    # def test_jump_others(self):
    #     self.page=UserPage(self.browser)
    #     self.page.jump_others('收货地址')
    def test_birthday(self):
        self.page=UserPage(self.browser)
        self.page.visit().select_birthday('1995-08-08')



    # @unittest.skip
    # def test_list(self):
    #     self.page1=ResultUserPage(self.browser)
    #     self.page1.visit().show_result_detail
    # @unittest.skip
    # def test_in_teble(self):
    #     # self.page=UserPage(self.browser)
    #     # self.page.search_user('zheng','188')
    #     self.page1=ResultUserPage(self.browser)
    #     self.page1.visit().is_intable('zhengzzzzzzz')
# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(Test("test_login"))
#     suite.addTest(Test("test_addbrand"))
#     suite.addTest(Test("test_jump"))
    #return suite
if __name__=='__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(suite())
    unittest.main()
