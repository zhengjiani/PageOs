# -*- coding: UTF-8 -*-
from __future__ import absolute_import
import os
import time
import unittest
from bok_choy.promise import BrokenPromise
from ddt import ddt,data,unpack
from bok_choy.web_app_test import WebAppTest
from tests.demo.page import LoginPage,HomePage,UserPage,ResultUserPage
from tests.demo.make_data import make_user_data
from ddt import ddt,unpack
@ddt
class Test(WebAppTest):
    def setUp(self):
        '''
        Instantiate the page object.
        :return:
        '''
        super(Test,self).setUp()
        self.login_page=LoginPage(self.browser)
        self.login_page.visit().login('','')
    @data(['cxiao123', '13839387456', '#@AZAfwy5d', '女', '普通用户', '可用', '1988-07-25'])
    @unpack
    def test_add_user(self,name,phone,passwd,gender_key,level_key,state_key,birthday):
        self.page = UserPage(self.browser)
        self.page.visit().add_user(name,phone,passwd,gender_key,level_key,state_key,birthday)
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
