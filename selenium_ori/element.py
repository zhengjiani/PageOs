# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 16:52
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):
    """BasePage会在每个页面对象类中进行初始化"""
    def __set__(self, instance, value):
        """将文本设置为提供的值"""
        driver = instance.driver
        WebDriverWait(driver,100).until(
            lambda driver:driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, instance, owner):
        """获取指定对象的文本"""
        driver = instance.driver
        WebDriverWait(driver,100).until(
            lambda driver:driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")