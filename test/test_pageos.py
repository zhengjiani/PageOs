# -*- encoding: utf-8 -*-
"""
@File    : test_pageos.py
@Time    : 2020/3/30 3:17 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import unittest
import requests


class TestPageApi(unittest.TestCase):
    def test_get_user(self):
        res = requests.get('http://127.0.0.1:5000/api/v1/user')
        response = res.json()
        print(response)
        self.assertEqual(response['msg'],"成功")

if __name__ == '__main__':
    unittest.main()