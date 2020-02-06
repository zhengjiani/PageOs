# -*- encoding: utf-8 -*-
"""
@File    : core.py
@Time    : 2020/1/11 2:14 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import datetime
import decimal
import uuid

from flask.json import JSONEncoder as BaseJSONEncoder
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class JSONEncoder(BaseJSONEncoder):
    """
    重新定义Flask json中default方法，支持更多转换方法
    """
    def default(self, o):
        """
        :param o:
        :return:
        """
        if isinstance(o,datetime.datetime):
            # 格式化时间
            return o.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(o,datetime.date):
            # 格式化日期
            return o.strftime('%Y-%m-%d')
        if isinstance(o,decimal.Decimal):
            # 格式化高精度数字
            return str(o)
        if isinstance(o,uuid.UUID):
            # 格式化uuid
            return str(o)
        if isinstance(o,bytes):
            # 格式化字节数据
            return o.decode("utf-8")
        return super(JSONEncoder, self).default(o)