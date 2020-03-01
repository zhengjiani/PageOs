# -*- encoding: utf-8 -*-
"""
@File    : __init__.py
@Time    : 2020/1/4 1:07 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from flask import Flask,current_app
from flask_sqlalchemy import SQLAlchemy
from config import config
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(config[config_name])
        config[config_name].init_app(app)
        db.init_app(app)

        from app.api import api as api_blueprint
        app.register_blueprint(api_blueprint,url_prefix='/api/v1')

    return app


