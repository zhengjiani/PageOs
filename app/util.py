# -*- encoding: utf-8 -*-
"""
@File    : util.py
@Time    : 2020/3/16 4:16 PM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""

# route装饰器，定义json统一返回格式
from functools import wraps

import pymysql
from flask import jsonify
from app.response import ResMsg



def route(api, *args, **kwargs):
    """
    路由设置，统一返回格式
    :param api: 蓝图
    :param args:
    :param kwargs:
    :return:
    """
    kwargs.setdefault('strict_slashes',False)

    def decorator(f):
        @api.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            rv = f(*args, **kwargs)
            # 响应函数返回整数和浮点型
            if isinstance(rv,(int,float)):
                res = ResMsg()
                res.update(data = rv)
                return jsonify(res.data)
            # 响应函数返回元组
            elif isinstance(rv,tuple):
                # 判断是否为多个参数
                if len(rv) >= 3:
                    return jsonify(rv[0]), rv[1], rv[2]
                else:
                    return jsonify(rv[0]), rv[1]
            # 响应函数返回字典
            elif isinstance(rv, dict):
                return jsonify(rv)
            # 响应函数返回字节
            elif isinstance(rv, bytes):
                rv = rv.decode('utf-8')
                return jsonify(rv)
            else:
                return jsonify(rv)

        return wrapper

    return decorator

