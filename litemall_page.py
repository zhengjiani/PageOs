# -*- encoding: utf-8 -*-
"""
@File    : litemall_page.py
@Time    : 2019/11/4 2:04 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
class BasePage(object):
    def __init__(self,driver):
        self.driver = webdriver.Chrome()
    # 定位方法封装
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
class SearchPage(BasePage):
    username_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/section//div/div[1]/div[1]/input')
    phone_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input')
    search_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]')
    # 输入用户名
    def type_username(self,username):
        self.driver.find_element(*self.username_loc).send_keys(username)
    # 输入电话
    def type_phone(self,phone):
        self.driver.find_element(*self.phone_loc).send_keys(phone)
    # 点击查询
    def search(self):
        self.driver.find_element(*self.search_loc).click()




