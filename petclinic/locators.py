# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 8:37
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from selenium.webdriver.common.by import By

class Locators():

    VETER_LINK=(By.LINK_TEXT,'Veterinarians')
    ERROR_LINK=(By.LINK_TEXT,'Error')
    INPUT_LASTNAME = (By.ID,'lastName')
    FIND_BUTTON = (By.XPATH,'//*[@id="search-owner-form"]/div[2]/div/button')
    ADD_BUTTON=(By.CSS_SELECTOR,'body > div > div > a')
    INPUT_FIRSTNAME =(By.ID,'firstName')
    INPUT_ADDRESS = (By.ID, 'address')
    INPUT_CITY =  (By.ID,'city')
    INPUT_TELEPHONE = (By.ID,'telephone')
    ADDOWNER_BUTTON = (By.CSS_SELECTOR,'#add-owner-form > div:nth-child(2) > div > button')
    EDITO_BUTTON = (By.LINK_TEXT,'Edit Owner')
    ADDPET_BUTTON = (By.LINK_TEXT,'New Pet')
    EDITP_LINK = (By.LINK_TEXT,'Edit Pet')
    ADDVISIT_BUTTON = (By.XPATH,'/html/body/div/div/form/div[2]/div/button')
    UPDATE_BUTTON = (By.CSS_SELECTOR,'#add-owner-form > div:nth-child(2) > div > button')
    INPUT_NAME = (By.ID,'name')
    INPUT_BIRTHDATE = (By.ID,'birthDate')
    SELECT = (By.TAG_NAME,'select')
    PET_BUTTON = (By.CSS_SELECTOR,'body > div > div > form > div:nth-child(3) > div > button')
    INPUT_DATE = (By.ID,'date')
    INPUT_DESC = (By.ID,'description')
    TABLE_LOC = (By.ID,'owners')
