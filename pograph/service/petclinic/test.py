# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 10:55
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
import HtmlTestRunner
from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),".","."))
from pograph.service.petclinic import FindOwnersPage,AddOwnerPage,AddPetPage,\
    AddVisitPage,EditOwnerPage,EditPetPage


class PetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @unittest.skip(u"强制跳过示例")
    def test_01_find_valid_owners(self):
        driver = self.driver
        driver.get('http://localhost:8080/owners/find')
        find_page = FindOwnersPage(driver)
        find_page.find_lastname('zhengjiani')
        time.sleep(2)

    @unittest.skip(u"强制跳过示例")
    def test_02_find_invalid_owners(self):
        driver = self.driver
        driver.get('http://localhost:8080/owners/find')
        find_page = FindOwnersPage(driver)
        find_page.find_lastname('zhengjiani')
        message = find_page.check_invalid_lastname_message()
        self.assertEqual(message,"has not been found")

    @unittest.skip(u"强制跳过示例")
    def test_add_owner(self):
        driver = self.driver
        driver.get('http://localhost:8080/owners/new')
        add_page= AddOwnerPage(driver)
        add_page.add_owner('zheng','jiani','xian','hanzhong','188')
        time.sleep(2)

    @unittest.skip(u"强制跳过示例")
    def test_edit_owner(self):
        driver = self.driver
        driver.get('http://localhost:8080/owners/1/edit')
        edit_owner_page = EditOwnerPage(driver)
        edit_owner_page.edit_address('beijing')
        time.sleep(2)

    @unittest.skip(u"强制跳过示例")
    def test_add_pet(self):
        driver = self.driver
        driver.get('http://localhost:8080/owners/1/pets/new')
        add_pet_page = AddPetPage(driver)
        add_pet_page.add_pet('google','2019-06-12')
        time.sleep(2)

    @unittest.skip(u"强制跳过示例")
    def test_edit_pet(self):
        driver = self.driver
        driver.get('http://localhost:8080/owners/1/pets/1/edit')
        edit_pet_page = EditPetPage(driver)
        edit_pet_page.edit_birth_date('2019-06-22')
        time.sleep(2)

    @unittest.skip(u"强制跳过示例")
    def test_add_visit(self):
        driver = self.driver
        driver.get('http://localhost:8080/owners/1/pets/1/visits/new')
        add_visit_page = AddVisitPage(driver)
        add_visit_page.add_date('2019-06-22','one visit')
        time.sleep(2)


    def test_find_owner(self):
        driver = self.driver
        driver.get('http://localhost:8080/owners/find')
        find_page = FindOwnersPage(driver)
        list_page = find_page.find_list()
        list = list_page.list_detail()
        assert 'Betty Davis' in list


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/code/python/PageOs/petclinic/reports"))