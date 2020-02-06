# -*- encoding: utf-8 -*-
"""
@File    : model.py
@Time    : 2020/1/11 2:46 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from utils.core import db
# 新建PO
class PO(db.Model):
    """
    页面对象表
    """
    __tablename__ = 'po'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    po_name = db.Column(db.String(20), nullable=False) #pageobject name

# 新建导航图Graph
class NavGraph(db.Model):
    """
    导航图
    """
    __tablename__ = 'navgraph'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nav_name = db.Column(db.String(20), nullable=False)

# 测试路径Testpath
class TestPath(db.Model):
    """
    测试路径
    """
    __tablename__ = 'testpath'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    path_name = db.Column(db.String(20), nullable=False)

# 测试用例
class TestCase(db.Model):
    """
    测试用例
    """
    __tablename__ = 'testcase'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    case_name = db.Column(db.String(20), nullable=False)