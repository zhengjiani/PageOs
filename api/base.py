# -*- encoding: utf-8 -*-
"""
@File    : base.py
@Time    : 2020/1/11 5:12 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
"""
单表接口基础
"""
import logging
from flask import current_app, request
from sqlalchemy import inspect

from utils.res_code import ResponseCode
from utils.core import db
from flask.views import MethodView

from utils.response import ResMsg
from utils.util import view_route

logger = logging.getLogger(__name__)

