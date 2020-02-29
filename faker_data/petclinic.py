# -*- encoding: utf-8 -*-
"""
@File    : petclinic.py
@Time    : 2020/2/18 3:47 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from faker import Faker

# f = Faker(locale='zh_CN')
f = Faker()
print('-----Owner Form-----')
info_dict = {}
info_dict['first_name'] = f.first_name()
info_dict['last_name'] = f.last_name()
info_dict['address'] = f.street_address()
info_dict['city'] = f.city_suffix()
info_dict['telephone'] = f.phone_number()
print(info_dict)
