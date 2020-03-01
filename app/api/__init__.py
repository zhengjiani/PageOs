# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2020/2/28 7:34 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from flask import Blueprint

api = Blueprint('api',__name__)

from . import files,gentest,menus,pageos,pograph,users