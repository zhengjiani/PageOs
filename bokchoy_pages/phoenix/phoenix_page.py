# -*- encoding: utf-8 -*-
"""
@File    : phoenix_page.py
@Time    : 2020/4/22 4:45 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from bok_choy.page_object import PageObject, unguarded
class BasePage(PageObject):
    pass
class BoardsPage(BasePage):
    def add_new_board(self,board_name):
        '''
        :param board_name:
        :return: BoardsPage
        '''
    def sign_out(self):
        '''
        :return: LoginPage
        '''
    def goto_board_list(self):
        '''
        :return: BoardsListPage
        '''
    def view_all_boards(self):
        '''
        :return: BoardsPage
        '''
class BoardsListPage(BasePage):
    def add_new_list(self,list_name):
        '''
        :param list_name:
        :return: BoardsListPage
        '''
    def update_list(self,cur_list,new_list):
        '''
        :param cur_list:
        :param new_list:
        :return: BoardsListPage
        '''
    def add_new_card(self,list_name,card_text):
        '''
        :param list_name:
        :param card_text:
        :return: BoardsListPage
        '''
    def add_new_member(self,new_mem):
        '''
        :param new_mem:
        :return: BoardsListPage
        '''
    def goto_card(self,list_name,card_id):
        '''
        :param list_name:
        :param card_id:
        :return: CardDetails
        '''
    def open_new_form(self):
        '''
        :return: BoardsListPage
        '''
class CardDetails(PageObject):
    pass
class LoginPage(BasePage):
    def login(self,email,password):
        '''
        :param email:
        :param password:
        :return: BoardsPage
        '''
    def goto_signup(self):
        '''
        :return: SignUpPage
        '''
class SignUpPage(BasePage):
    def sign_up(self,first_name,last_name,email,password):
        '''
        :param first_name:
        :param last_name:
        :param email:
        :param password:
        :return: BoardsPage
        '''
    def goto_login(self):
        '''
        :return: LoginPage
        '''