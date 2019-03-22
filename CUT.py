# -*- coding: utf-8 -*-
"""
input:POs
input:SigninPage,UserViewPage,PasswordPage,UserManagerPage,UserResultPage
output:class CUT
methon:POmethod,return type:void
调用这些方法的条件是：当前PO对象是该PO对象原属方法的实例

"""

from bok_choy.page_object import PageObject
from __future__ import absolute_import
from bok_choy.web_app_test import WebAppTest



class CUT:
    def __init__(self,currentPage):
        self.__currentPage = currentPage
    def sign_in(self,username,password):
        if isinstance(self.__currentPage,SigninPage):
            page = SigninPage(self.browser)
            dict = page.sign_in(username, password)
            if  dict['username']==username and dict['password']==password:

                self.__currentPage=ProductPage(self.browser)
            else:
                raise ValueError("Invalid parameter values")
        else:
            raise ValueError("You are not in right Page")