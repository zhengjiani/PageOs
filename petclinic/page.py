# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 9:14
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
import inspect
import sys
from petclinic.locators import Locators
import time
class FindOwnersPage():

    def __init__(self,driver):
        self.driver = driver
        self.inValidLastname_message_xpath = "//*[@id='lastNameGroup']/div/span/div/p"

    def find_lastname(self,lastname):
        self.driver.find_element(*Locators.INPUT_LASTNAME).clear()
        self.driver.find_element(*Locators.INPUT_LASTNAME).send_keys(lastname)
        self.driver.find_element(*Locators.FIND_BUTTON).click()

    def find_list(self):
        self.driver.find_element(*Locators.FIND_BUTTON).click()
        return OwnersListPage(self.driver)
    def check_invalid_lastname_message(self):
        msg = self.driver.find_element_by_xpath(self.inValidLastname_message_xpath).text
        return msg
class OwnersListPage():

    def __init__(self,driver):
        self.driver = driver

    def list_detail(self):
        table = self.driver.find_element(*Locators.TABLE_LOC)
        rows = table.find_elements_by_tag_name("tr")
        rowname = []
        for row in rows[1:]:
            col = row.find_element_by_xpath("td[1]/a")
            rowname.append(col.text)
        return rowname
class AddOwnerPage():

    def __init__(self,driver):
        self.driver = driver

    def add_owner(self,firstName,lastName,address,city,telephone):
        self.driver.find_element(*Locators.INPUT_FIRSTNAME).send_keys(firstName)
        self.driver.find_element(*Locators.INPUT_LASTNAME).send_keys(lastName)
        self.driver.find_element(*Locators.INPUT_ADDRESS).send_keys(address)
        self.driver.find_element(*Locators.INPUT_CITY).send_keys(city)
        self.driver.find_element(*Locators.INPUT_TELEPHONE).send_keys(telephone)
        self.driver.find_element(*Locators.ADDOWNER_BUTTON).click()

class EditOwnerPage():
    def __init__(self,driver):
        self.driver = driver

    def edit_firstname(self,firstName):
        self.driver.find_element(*Locators.INPUT_FIRSTNAME).clear()
        self.driver.find_element(*Locators.INPUT_FIRSTNAME).send_keys(firstName)

    def edit_lastname(self,lastName):
        self.driver.find_element(*Locators.INPUT_LASTNAME).clear()
        self.driver.find_element(*Locators.INPUT_LASTNAME).send_keys(lastName)

    def edit_address(self,address):
        self.driver.find_element(*Locators.INPUT_ADDRESS).clear()
        self.driver.find_element(*Locators.INPUT_ADDRESS).send_keys(address)

    def edit_city(self,city):
        self.driver.find_element(*Locators.INPUT_CITY).clear()
        self.driver.find_element(*Locators.INPUT_CITY).send_keys(city)

    def edit_telephone(self,telephone):
        self.driver.find_element(*Locators.INPUT_TELEPHONE).clear()
        self.driver.find_element(*Locators.INPUT_TELEPHONE).send_keys(telephone)

class AddPetPage():
    def __init__(self,driver):
        self.driver = driver

    def add_pet(self,name,birthDate):
        time.sleep(5)
        self.driver.find_element(*Locators.INPUT_NAME).send_keys(name)
        self.driver.find_element(*Locators.INPUT_BIRTHDATE).send_keys(birthDate)
        # self.driver.find_element(*Locators.SELECT).select_by_index(1)
        self.driver.find_element(*Locators.PET_BUTTON).click()

class EditPetPage():
    def __init__(self,driver):
        self.driver = driver

    def edit_pet_name(self,name):
        self.driver.find_element(*Locators.INPUT_NAME).clear()
        self.driver.find_element(*Locators.INPUT_NAME).send_keys(name)

    def edit_birth_date(self,birthDate):
        self.driver.find_element(*Locators.INPUT_BIRTHDATE).clear()
        self.driver.find_element(*Locators.INPUT_NAME).send_keys(birthDate)

class AddVisitPage():
    def __init__(self,driver):
        self.driver = driver

    def add_date(self,date,description):
        self.driver.find_element(*Locators.INPUT_DATE).clear()
        self.driver.find_element(*Locators.INPUT_DATE).send_keys(date)
        self.driver.find_element(*Locators.INPUT_DESC).send_keys(description)
        self.driver.find_element(*Locators.ADDVISIT_BUTTON).click()



if __name__ == '__main__':
    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    nodes = []
    # print(clsmembers)
    for class_name in clsmembers:
        if class_name[0].endswith('Page'):
            # print(class_name[0])
            nodes.append(class_name[0])
    # print(nodes)
    for page in nodes:
        funmembers = inspect.getmembers(eval(page),inspect.isfunction)
        # print(funmembers)
        dic = {}
        edges = []
        for func in funmembers:
            if func[0] != '__init__':
                edges.append(func[0])
            dic[page]=edges
        print(dic)