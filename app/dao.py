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

def map_user(x):
    a =  {'id': x[0], 'username': x[1], 'password': x[2], 'public_id': x[3]}
    return a

def map_pog(x):
    a = {'id':x[0],'pagename':x[1],'file_path':x[2],'graph_path':x[3]}
    return a

def map_dic(x):
    a = {'id': x[0], 'pagename': x[1], 'pog': x[2]}
    return a

def get_users():
    cursor = CONN.cursor()
    sql = 'SELECT * from users ORDER BY id desc'
    cursor.execute(sql)
    output = cursor.fetchall()
    return list(mapping(output))

def check_id_existence(cursor,user_id):
    sql = 'SELECT * FROM users WHERE public_id = %s'
    cursor.execute(sql,[user_id,])
    result = cursor.fetchall()
    if len(result) == 0:
        raise Exception('user not exist')
def get_user_by_id(user_id):
    cursor = CONN.cursor()
    check_id_existence(cursor,user_id)
    sql = 'SELECT * FROM users WHERE public_id = %s'
    cursor.execute(sql,[user_id,])
    user = cursor.fetchone()
    return user

def get_user_by_name(name):
    cursor = CONN.cursor()
    sql = 'SELECT * FROM users WHERE username = %s'
    cursor.execute(sql,[name,])
    user = cursor.fetchone()
    return map_user(user)

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

def get_pog_by_id(pog_id):
    cursor = CONN.cursor()
    sql = 'SELECT * FROM pages WHERE id = %s'
    cursor.execute(sql, [pog_id, ])
    pog = cursor.fetchone()
    return map_pog(pog)

def get_pog_by_name(pog_name):
    cursor = CONN.cursor()
    sql = 'SELECT * FROM pages WHERE pagename = %s'
    cursor.execute(sql, [pog_name, ])
    pog = cursor.fetchone()
    return map_pog(pog)

def get_dict_by_name(pog_name):
    cursor = CONN.cursor()
    sql = 'SELECT * FROM graphs WHERE pagename = %s'
    cursor.execute(sql, [pog_name, ])
    pog = cursor.fetchone()
    return map_dic(pog)

if __name__ == '__main__':
    # print(get_user_by_id('04bcac0d-5180-48e5-8a08-575054e3ecc2'))
    # print(get_user_by_name('admin1'))
    # print(get_pog_by_id(2))
    # print(get_pog_by_name('pageKit_page'))
    print(get_dict_by_name('pageKit_page'))

