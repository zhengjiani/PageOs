# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 16:46
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from .element import BasePageElement
from .locators import MainPageLocators

class SearchTextElement(BasePageElement):
    locator = 'q'

class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultsPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source