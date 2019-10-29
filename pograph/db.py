# -*- encoding: utf-8 -*-
"""
@File    : demo1.py
@Time    : 2019/10/24 9:02 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# SQLite数据库
import sqlite3

import click
from flask import current_app,g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db',None)
    if db is not None:
        db.close()

# 运行SQL命令
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# 清除已存在的数据创建新表
# 定义一个名为init-db的命令行，调用init_db函数
@click.command('init-db')
@with_appcontext
def init_db_command():
    """删除已存在的数据并创建新表"""
    init_db()
    click.echo('初始化数据库')

# 把应用作为参数，在函数中注册
def init_app(app):
    # 告诉flask在返回响应进行清理时调用此函数
    app.teardown_appcontext(close_db)
    # 添加一个新的可以和Flask一起工作的命令
    app.cli.add_command(init_db_command)

