# -*- coding: utf-8 -*-
# @Time    : 2019/6/6 16:22
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
import inspect
import os
import random
import sys

from bok_choy.page_object import PageObject, unguarded


class BasePage(PageObject):
    SERVER_PORT = os.environ.get("SERVER_PORT", 3000)
    @property
    def url(self):
        return "http://localhost:{0}/#!/{1}".format(self.SERVER_PORT, self.name)

class InputOwnerPage(PageObject):
    url = None

    @unguarded
    def input_info(self,first_name,last_name,address,city,telephone):
        self.q(xpath='//input[@name="firstName"]').fill(first_name)
        self.q(xpath='//input[@name="lastName"]').fill(last_name)
        self.q(xpath='//input[@name="address"]').fill(address)
        self.q(xpath='//input[@name="city"]').fill(city)
        self.q(xpath='//input[@name="telephone"]').fill(telephone)

    @unguarded
    def submit(self):
        self.q('(//button)[2]').click()

class InputPetPage(PageObject):
    url = None

    @unguarded
    def input_info(self,pet_name,birth_date,pet_type):
        self.q(xpath='//input[@name="name"]').fill(pet_name)
        self.q(xpath='//label[text()="Birth date"]/following-sibling::div/input').fill(birth_date)
        self.q(xpath='//select/option[text()="{}"]'.format(pet_type)).first.click()

    @unguarded
    def submit(self):
        self.q('(//button)[2]').click()



class HomePage(BasePage):
    name = "welcome"

    def is_browser_on_page(self):
        h1_text = "Petclinic"
        return h1_text in self.q("//h1").text

    def goto_search(self):
        '''
        :return: FindPage
        '''
        self.q(xpath='//a[span=" All"]').click()
        return FindPage(self.browser).wait_for_page()

    def goto_register(self):
        '''
        :return: RegisterPage
        '''
        self.q(xpath='//a[span=" Register"]').click()
        return RegisterPage(self.browser).wait_for_page()

    def goto_Veter(self):
        '''
        :return: VeterPage
        '''
        self.q(xpath='//a[span="Veterinarians"]').click()
        return VeterPage(self.browser).wait_for_page()


class FindPage(BasePage):
    name = "owners"

    def is_browser_on_page(self):
        return "Owners" in self.q('//h2').text

    def find_owner(self, first_name):
        self.q(xpath='//input').fill(first_name)

    def get_owners(self):
        owners = []
        els = self.q(xpath='//table/tbody/tr')
        for el in els:
            owners.append(el.text)
        return owners

    def goto_detail_page(self, owner):
        '''
        :param owner: firstname lastname
        :return: DetailPage
        '''
        self.q(xpath='//tbody/tr/td/a[contains(text(),"{}")]'.format(owner))
        return DetailPage(self.browser).wait_for_page()

class RegisterPage(BasePage):
    name = "owners/new"

    def is_browser_on_page(self):
        return self.q(xpath='/html/body/div/div/div/ui-view/owner-form/h2').is_present

    def regist_owner(self, owner_info):
        '''
        :param owner_info: dict,keys:first_name,last_name,address,city,telephone
        :return: FindPage
        '''
        first_name = owner_info.get("first_name")
        last_name = owner_info.get("last_name")
        address = owner_info.get("address")
        city = owner_info.get("city")
        telephone = owner_info.get("telephone")
        InputOwnerPage.input_info(first_name,last_name,address,city,telephone)
        InputOwnerPage.submit()

        return FindPage(self.browser).wait_for_page()

class DetailPage(BasePage):

    name = "owners/details/1"

    def is_browser_on_page(self):
        label = self.q(xpath='(//h2)[1]').text
        return label == ['Owner Information']

    @unguarded
    def get_owner_info(self):
        infos = []
        els = self.q(xpath='(//tbody)[1]/tr')
        for i in range(len(els)):
            tr = self.q('((//tbody)[1]/tr)[i]'.format(i)).text
            infos.append(tr)
        return infos

    @unguarded
    def get_pets_info(self):
        infos = []
        els = self.q(xpath='(//tbody)[2]/tr')
        for i in range(len(els)):
            tr = self.q('((//tbody)[2]/tr)[{}]'.format(i)).text
            infos.append(tr)
        return infos

    def goto_edit(self):
        '''
        :return: EditOwnerPage
        '''
        self.q(xpath='//a[text()="Edit Owner"]').click()
        return EditOwnerPage(self.browser).wait_for_page()

    def goto_add_pet(self):
        '''
        :return: AddNewPetPage
        '''
        self.q(xpath='//a[text()="Add New Pet"]').click()
        return AddNewPetPage(self.browser).wait_for_page()

    def goto_edit_pet(self,pet):
        '''
        :param pet: pet_name
        :return: PetPage
        '''
        els = self.q(xpath='(//tbody)[2]/tr')
        for el in range(len(els)):
            if pet == self.q(xpath='((//dt[text()="Name"])[{}]/following-sibling::dd)[1]/a'.format(el)).text:
                loc = el
                self.q(xpath='//a[@href="#!/owners/1/pets/{}'.format(loc)).click()
                return PetPage(self.browser).wait_for_page()

    def goto_visit(self,pet):
        '''
        :param pet: pet_name
        :return: AddNewVisitPage
        '''
        els = self.q(xpath='(//tbody)[2]/tr')
        for el in range(len(els)):
            if pet == self.q(xpath='((//dt[text()="Name"])[{}]/following-sibling::dd)[1]/a'.format(el)).text:
                pet_loc = el
                self.q(xpath='//a[@href="#!/owners/1/pets/{}/visits"]'.format(pet_loc)).click()
                return AddNewVisitPage(self.browser).wait_for_page()

    def goto_pet(self,pet):
        '''
        :param pet: pet_name
        :return: PetPage
        '''
        els = self.q(xpath='(//tbody)[2]/tr')
        for el in range(len(els)):
            if pet == self.q(xpath='((//dt[text()="Name"])[{}]/following-sibling::dd)[1]/a'.format(el)).text:
                self.q(xpath='((//dt[text()="Name"])[{}]/following-sibling::dd)[1]/a'.format(el)).click()
                return PetPage(self.browser).wait_for_page()

class EditOwnerPage(BasePage):

    name = "owners/1/edit"

    def is_browser_on_page(self):
        label = self.q(xpath=self.el + 'h2').text
        return label == ['Owner']

    def edit_info(self, edit_info):
        '''
        :param edit_info: type(edit_info)
        :return: DetailPage
        '''
        first_name = edit_info.get("first_name")
        last_name = edit_info.get("last_name")
        address = edit_info.get("address")
        city = edit_info.get("city")
        telephone = edit_info.get("telephone")
        InputOwnerPage.input_info(first_name, last_name, address, city, telephone)
        InputOwnerPage.submit()

        return DetailPage(self.browser).wait_for_page()


class AddNewPetPage(BasePage):
    name = "owners/2/new-pet"

    def is_browser_on_page(self):
        label = self.q(xpath=self.el + 'h2').text
        return label == ['Pet']

    def add_new_pet(self, pet_info):
        '''
        :param pet_info: type dict pet_name,birth_date,pet_type
        :return: DetailPage
        '''
        pet_name = pet_info.get("pet_name")
        birth_date = pet_info.get("birth_date")
        pet_type = pet_info.get("pet_type")
        InputPetPage.input_info(pet_name,birth_date,pet_type)
        InputPetPage.submit()
        return DetailPage(self.browser).wait_for_page()

class PetPage(BasePage):

    name = "owners/2/pets/1"

    def is_browser_on_page(self):
        label = self.q(xpath=self.el + 'h2').text
        return label == ['Pet']

    def edit_pet(self, pet_info):
        '''
        :param pet_info: type dict pet_name,birth_date,pet_type
        :return: DetailPage
        '''
        pet_name = pet_info.get("pet_name")
        birth_date = pet_info.get("birth_date")
        pet_type = pet_info.get("pet_type")
        InputPetPage.input_info(pet_name,birth_date,pet_type)
        InputPetPage.submit()
        return DetailPage(self.browser).wait_for_page()

class AddNewVisitPage(BasePage):

    url = "owners/2/pets/1/visits"

    def is_browser_on_page(self):
        label = self.q(xpath=self.el + 'h2').text
        return label == ['Visits']

    def add_visit(self, date, desc):
        '''
        :param date: visit date
        :param desc: visit description
        :return: DetailPage
        '''
        self.q(xpath='//label[text()="Date"]/following-sibling::input').fill(date)
        self.q(xpath='//label[text()="Description"]/following-sibling::input').fill(desc)
        self.q(xpath='(//button)[2]').click()
        return DetailPage(self.browser).wait_for_page()

    def get_visits(self):
        # late_date
        late_date = self.q(xpath=self.el + 'table/tbody/tr[1]/td[1]').text
        desc = self.q(xpath=self.el + 'table/tbody/tr[1]/td[2]').text
        return late_date, desc

class VeterPage(BasePage):
    name = "owners/1/pets/1/visits"
    def get_veters(self):
        veters = []
        els = self.q(xpath='//tbody/tr')
        for el in range(1,len(els)):
            veters.append(self.q(xpath='//tbody/tr[{}]'.format(el)).text)
        return veters
