# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 16:07
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from bok_choy.page_object import PageObject
class LoginPage(PageObject):
    url = "http://zhengjiani.cn:8081/"
    def is_browser_on_page(self):
        pass
    def login(self,username,password):
        self.q(xpath='//*[@id="LoginForm"]/input[1]').fill(username)
        self.q(xpath='//*[@id="LoginForm"]/input[1]').fill(password)

        #btn
class RegisterPage(PageObject):
    url = "http://zhengjiani.cn:8081/"
    def is_browser_on_page(self):
        pass
    def regist(self,username,password):
        self.q(xpath='//*[@id="LoginForm"]/input[1]').fill(username)
        self.q(xpath='//*[@id="LoginForm"]/input[1]').fill(password)
        #btn
class HomePage(PageObject):
    url = "http://zhengjiani.cn:8081/"
    def is_browser_on_page(self):
        pass
    def select_user(self):
        self.q(xpath='//*[@id="1"]').click()
    def delete(self):
        self.q(xpath='//*[@id="1"]').click()
        self.q(xpath='//*[@id="content"]/form[2]/div[2]/input').click()
    def senf_email(self):
        self.q(xpath='//*[@id="content"]/form[2]/div[1]/input').click()
    def add(self):
        self.q(xpath='//*[@id="content"]/form[2]/div[4]/input').click()
    def logout(self):
        self.q(xpath='//*[@id="top"]/form/a').click()
    def search(self):
        self.q(xpath='//*[@id="search-az"]/form/input').click()
class EditPage(PageObject):
    url = "http://zhengjiani.cn:8081/edit.php"
    def is_browser_on_page(self):
        pass
    def add(self,address,name):
        # 20个框框
        self.q(xpath='//*[@id="content"]/form/textarea').fill(address)
        self.q(xpath='//*[@id="content"]/form/input[2]').click()
        self.q(xpath='//*[@id="content"]/form/input[2]').fill(name)
        self.q(xpath='//*[@id="content"]/form/input[21]').click()
class GroupPage(PageObject):
    url = "http://zhengjiani.cn:8081/group.php"
    def is_browser_on_page(self):
        pass
    def add_group(self,name,logo,comment):
        self.q(xpath='//*[@id="content"]/form/input[1]').click()
        self.q(xpath='//*[@id="content"]/form/input[1]').fill(name)
        # select group
        self.q(xpath='//*[@id="content"]/form/textarea[1]').fill(logo)
        self.q(xpath='//*[@id="content"]/form/textarea[2]').fill(comment)
    def delete_group(self):
        pass
    def edit_group(self,name,logo,comment):
        self.q(xpath='//*[@id="content"]/form/input[3]').click()
        self.q(xpath='//*[@id="content"]/form/input[1]').fill(name)
        # select group
        self.q(xpath='//*[@id="content"]/form/textarea[1]').fill(logo)
        self.q(xpath='//*[@id="content"]/form/textarea[2]').fill(comment)
class BirthdaysPage(PageObject):
    url = "http://zhengjiani.cn:8081/birthdays.php"
    def is_browser_on_page(self):
        pass
class ExportPage(PageObject):
    url = "http://zhengjiani.cn:8081/export.php"
    def is_browser_on_page(self):
        pass
    def download(self):
        self.q(xpath='//*[@id="content"]/form[4]/input[2]').click()
class ImportPage(PageObject):
    url = "http://zhengjiani.cn:8081/import.php"
    def is_browser_on_page(self):
        pass
    def download(self):
        self.q(xpath='//*[@id="file"]').click()
        # upload
        self.q(xpath='//*[@id="content"]/form/input[3]').click()
class PrintPage(PageObject):
    url = "http://zhengjiani.cn:8081/view.php?all&print&phones"
    def is_browser_on_page(self):
        pass
    def print(self):
        pass
