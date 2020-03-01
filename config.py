# -*- encoding: utf-8 -*-
"""
@File    : config.py
@Time    : 2020/2/29 11:43 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:ZhengJiaNi@88@localhost:3306/flask_pos?charset=utf8'

config = {
    'default' : DevelopmentConfig
}