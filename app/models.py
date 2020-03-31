# -*- encoding: utf-8 -*-
"""
@File    : models.py
@Time    : 2020/2/29 11:49 PM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from . import db

class User(db.Model):

    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32),index=False,unique=True,nullable=False)
    password = db.Column(db.String(128), index=False, unique=True, nullable=False)
    public_id = db.Column(db.String(50), index=False, unique=True, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Page(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.Integer, primary_key=True)
    pagename = db.Column(db.String(32), index=True)
    file_path = db.Column(db.String(128))

    def __repr__(self):
        return '<Page {}>'.format(self.pagename)
