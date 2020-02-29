# -*- encoding: utf-8 -*-
"""
@File    : config.py
@Time    : 2020/2/29 11:43 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import os

USERNAME = 'root'  # 用户名
PASSWORD = 'ZhengJiaNi@88'  # 密码
HOST = 'localhost'  # 数据库地址
PORT = '3306'  # 端口
DATABASE = 'flask_pos'  # 数据库名
database_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOST, PORT, DATABASE
)
class Config:
    SECRET_KEY = 'the quick brown fox jumps over the lazy dog'
    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
