# -*- encoding: utf-8 -*-
"""
@File    : dao.py
@Time    : 2020/3/17 11:29 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import pymysql

from app import db

CONN = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='ZhengJiaNi@88',
                       database='flask_pos',
                       charset='utf8'
                       )

def mapping(output):
    a = map(lambda x: {'id': x[0], 'username': x[1], 'password': x[2], 'public_id': x[3], 'admin': x[4]},output)
    return a

def get_users():
    cursor = CONN.cursor()
    sql = 'SELECT * from users ORDER BY id desc'
    cursor.execute(sql)
    output = cursor.fetchall()
    return list(mapping(output))

def check_existence(cursor,user_id):
    sql = 'SELECT * FROM users WHERE public_id = %s'
    cursor.execute(sql,[user_id,])
    result = cursor.fetchall()
    if len(result) == 0:
        raise Exception('user not exist')

def get_user(user_id):
    cursor = CONN.cursor()
    check_existence(cursor,user_id)
    sql = 'SELECT * FROM users WHERE public_id = %s'
    cursor.execute(sql,[user_id,])
    user = cursor.fetchone()
    return user

def add_user(data):
    try:
        cursor = CONN.cursor()
        sql = 'INSERT INTO users (public_id,username,password,admin) values (%s,%s,%s,%s)'
        cursor.execute(sql,[data['public_id'], data['username'], data['password'], data['admin'],])
        CONN.commit()
        output = None
    except Exception as e:
        output = "error"
    return output

