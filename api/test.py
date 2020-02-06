# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2020/1/11 12:03 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from flask import Blueprint
from utils.util import route
from utils.response import ResMsg
from utils.res_code import ResponseCode
from datetime import datetime
from decimal import Decimal

bp = Blueprint(service_name, __name__, url_prefix="/")

@route(bp, '/packed_response', methods=["GET"])
def test_packed_response():
    """
    测试响应封装
    :return:
    """
    res = ResMsg()
    test_dict = dict(name="zhang",age=18)
    # 填入响应码，可以获得对应的响应信息
    res.update(code=ResponseCode.SUCCESS, data=test_dict)
    # 如果需要定制返回头或http响应
    # return res.data,200,{"token":"111"}
    return res.data

@route(bp, '/type_response', methods=['GET'])
def test_type_response():
    """
    测试返回不同的类型
    :return:
    """
    res = ResMsg()
    now = datetime.now()
    date = datetime.now().date()
    num = Decimal(11.11)
    test_dict = dict(now=now,date=date,num=num)
    res.update(code=ResponseCode.SUCCESS,data=test_dict)
    return res.data