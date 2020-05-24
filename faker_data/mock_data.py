# -*- encoding: utf-8 -*-
"""
@File    : mock_data.py
@Time    : 2020/5/6 9:49 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from faker import Faker
def make_data(params):
    """
    :param params: list
    :return: dict
    """
    f = Faker()
    info_dict = {}
    data_dict = {}
    info_dict["firstname"] = f.first_name()
    info_dict["lastname"] = f.last_name()
    info_dict["pet_name"] = f.name()
    info_dict["date"] = f.date()
    info_dict["desc"] = f.text()
    for s in params:
        for k,v in info_dict.items():
            if s == k:
                data_dict[s] = v
    return data_dict

if __name__ == '__main__':
    print(make_data(["firstname"]))
