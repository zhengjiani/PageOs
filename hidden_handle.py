# -*- coding: UTF-8 -*-
from selenium import webdriver
import time,os

driver=webdriver.Firefox()
driver.get('http://localhost:9527/#/login?redirect=%2Fdashboard')
driver.find_element_by_xpath('//*[@id="app"]/div/form/button').click()
driver.get('http://localhost:9527/#/user/user')
#time.sleep(5)
arr=[]
arr1=[]
tr_list=driver.find_elements_by_tag_name("tr")
for tr in tr_list:
    arr1=(tr.text).split(" ")
    arr.append(arr1)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j])





