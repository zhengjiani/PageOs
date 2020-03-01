# -*- encoding: utf-8 -*-
"""
@File    : models.py
@Time    : 2020/2/29 11:52 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from app import db

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password = db.Column(db.String(128))
    public_id = db.Column(db.String(50), unique=True)
    admin = db.Column(db.Boolean)
    extend_existing = True

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Page(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.Integer, primary_key=True)
    pagename = db.Column(db.String(32), index=True)
    file_path = db.Column(db.String(128))

    def __repr__(self):
        return '<Page {}>'.format(self.pagename)
