# -*- coding: utf-8 -*-
# @Time    : 2019/6/6 16:22
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from bok_choy.page_object import PageObject


class BasePage(PageObject):
    @property
    def url(self):
        return "http://localhost:8080/{0}".format(self.name)
class HomePage(PageObject):
    """主页"""
    url = "http://localhost:8080/"
    def is_browser_on_page(self):
        return self.q(xpath='/html/body/div/div/div[2]/div/div/img').is_present
class FindPage(PageObject):
    """查找页面对象"""
    url = "http://localhost:8080/owners/find"
    def is_browser_on_page(self):
        return self.q(xpath='/html/body/div/div/a').is_present
    def find_owner(self,last_name):
        self.q(xpath='//*[@id="lastName"]').fill(last_name)
        self.q(xpath='//*[@id="search-owner-form"]/div[2]/div/button').click()
    def add_owner(self):
        self.q(xpath='/html/body/div/div/a').click()
class AddPage(PageObject):
    url = "http://localhost:8080/owners/new"
    def is_browser_on_page(self):
        return self.q(xpath='/html/body/div/div/h2').is_present
    def add(self,first_name,last_name,address,city,telephone):
        self.q(xpath='//*[@id="firstName"]').fill(first_name)
        self.q(xpath='//*[@id="lastName"]').fill(last_name)
        self.q(xpath='//*[@id="address"]').fill(address)
        self.q(xpath='//*[@id="city"]').fill(city)
        self.q(xpath='//*[@id="telephone"]').fill(telephone)
        self.q(xpath='//*[@id="add-owner-form"]/div[2]/div/button').click()
class OwnerPage(PageObject):
    """个人主页"""
    url = "http://localhost:8080/owners/12"
    def is_browser_on_page(self):
        return self.q(xpath='/html/body/div/div/h2[1]').is_present
    def edit_owner(self):
        self.q(xpath='/html/body/div/div/a[1]').click()
    def add_visit(self):
        self.q(xpath='/html/body/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td[2]/a').click()
class EditOwnerPage(PageObject):
    """更改个人信息页"""
    url = "http://localhost:8080/owners/12/edit"
    def is_browser_on_page(self):
        return self.q(xpath='/html/body/div/div/h2').is_present
    def edit(self,first_name,last_name,address,city,telephone):
        self.q(xpath='//*[@id="firstName"]').fill(first_name)
        self.q(xpath='//*[@id="lastName"]').fill(last_name)
        self.q(xpath='//*[@id="address"]').fill(address)
        self.q(xpath='//*[@id="city"]').fill(city)
        self.q(xpath='//*[@id="telephone"]').fill(telephone)
        self.q(xpath='//*[@id="add-owner-form"]/div[2]/div/button').click()
    def add_pet(self):
        self.q(xpath='/html/body/div/div/a[2]').click()
class PetPage(PageObject):
    """个人宠物页"""
    def is_browser_on_page(self):
        return self.q(xpath='/html/body/div/div/h2').is_present
    def select_type(self,pet_value):
        self.q(css=u'select[name="cars"] option[value="{}"]'.format(pet_value)).first.click()
    def add(self,name,date,type):
        self.q(xpath='//*[@id="name"]').fill(name)
        self.q(xpath='//*[@id="birthDate"]').fill(date)
        self.select_type(type)
        self.q(xpath='/html/body/div/div/form/div[2]/div/button').click()
class EditPetPage(PageObject):
    """更改宠物信息页"""
    url = "http://localhost:8080/owners/1/pets/1/edit"
    def is_browser_on_page(self):
        return self.q(xpath='/html/body/div/div/h2').is_present
    def edit(self,name,date,type):
        self.q(xpath='/html/body/div/div/a[2]').click()
        self.q(xpath='//*[@id="name"]').fill(name)
        self.q(xpath='//*[@id="birthDate"]').fill(date)
        self.select_type(type)
        self.q(xpath='/html/body/div/div/form/div[2]/div/button').click()
class VisitPage(PageObject):
    """访问页"""
    url = "http://localhost:8080/owners/12/pets/15/visits/new"
    def is_browser_on_page(self):
        return self.q(xpath='/html/body/div/div/h2').is_present
    def add(self,date,desc):
        self.q(xpath='//*[@id="date"]').fill(date)
        self.q(xpath='//*[@id="description"]').fill(desc)
        self.q(xpath='/html/body/div/div/form/div[2]/div/button').click()
class VetsPage(PageObject):
    url = "http://localhost:8080/vets.html"
    def is_browser_on_page(self):
        label = self.q(xpath='/html/body/div/div/h2').text
        return label == ['Veterinarians']
class ErrorPage(PageObject):
    url = "http://localhost:8080/oups"
    def is_browser_on_page(self):
        return self.q(xpath='/html/body/div/div/img').is_present
