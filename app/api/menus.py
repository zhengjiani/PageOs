# -*- encoding: utf-8 -*-
"""
@File    : menus.py
@Time    : 2020/2/28 7:35 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from flask import jsonify, Blueprint, Response, request
from . import api
from ..code import ResponseCode
from ..response import ResMsg
from ..util import route


@route(api,'/menus',methods=['GET'])
def get_menus():
    res = ResMsg()
    res_dict =[
        {
            "id": 101,
            "authName": "页面对象",
            "path": None,
            "children": [
                {
                    "id": 104,
                    "authName": "页面对象自动生成",
                    "path": "auto",
                    "children": []
                },
                {
                    "id": 105,
                    "authName": "页面对象手动编写",
                    "path": "manual",
                    "children": []
                },
                {
                    "id": 106,
                    "authName": "页面对象文件管理",
                    "path": "pageos",
                    "children": []
                }
            ]
        },
        {
            "id": 102,
            "authName": "Web应用导航图",
            "path": None,
            "children": [
                {
                    "id": 107,
                    "authName": "Web应用导航图生成",
                    "path": "graph",
                    "children": []
                },
                {
                    "id": 108,
                    "authName": "Web应用导航图管理",
                    "path": "graphli",
                    "children": []
                }
            ]
        },
        {
            "id": 103,
            "authName": "Web测试用例生成",
            "path": None,
            "children": [
                {
                    "id": 109,
                    "authName": "测试路径提取",
                    "path": "pathsGraph",
                    "children": []
                },
                {
                    "id": 110,
                    "authName": "测试用例生成",
                    "path": "testCase",
                    "children": []
                }
            ]
        }
    ]
    res.update(code=ResponseCode.SUCCESS, data=res_dict)
    return res.data
