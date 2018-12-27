# -*- coding: utf-8 -*-
from selenium import webdriver
dr=webdriver.Chrome()
dr.get('http://localhost:9527/#/login?redirect=%2Fdashboard')
dr.find_element_by_xpath('//*[@id="app"]/div/form/button').click()
dr.get('http://localhost:9527/#/goods/create')
dr.implicitly_wait(5)
dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[5]/div/div/label[1]/span[1]/span').click()