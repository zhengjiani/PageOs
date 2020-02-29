# -*- encoding: utf-8 -*-
"""
@File    : app.py
@Time    : 2020/1/4 1:07 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import *
from resources import files,gentest,menus,pageos,pograph,users

app = Flask(__name__)

app.register_blueprint(users.users)
app.register_blueprint(files.files)
app.register_blueprint(gentest.gentest)
app.register_blueprint(menus.menus)
app.register_blueprint(pageos.pageos)
app.register_blueprint(pograph.pograph)

CORS(app, supports_credentials=True)

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)
app.json_encoder = MyEncoder

db = SQLAlchemy(app)
app.config.from_object('config.Config')
db.init_app(app)
db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
