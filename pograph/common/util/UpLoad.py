# -*- coding: utf-8 -*-
from selenium import webdriver
import win32gui
import win32con
import time

# dr = webdriver.Chrome()
# dr.get('http://localhost:9527/#/login?redirect=%2Fdashboard')
# dr.find_element_by_xpath('//*[@id="app"]/div/form/button').click()
# dr.get('http://localhost:9527/#/mall/brand')
# dr.implicitly_wait(10)
# dr.find_element_by_css_selector(
#     '#app > div > div.main-container > section > div > div.filter-container > button:nth-child(4)').click()
# upload = dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div')
# upload.click()
# time.sleep(1)
def upload(abspath):
    dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, abspath)  # 往输入框输入绝对地址
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
