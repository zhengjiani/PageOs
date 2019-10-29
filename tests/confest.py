# -*- encoding: utf-8 -*-
"""
@File    : confest.py
@Time    : 2019/10/28 4:16 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# app 固件会调用工厂并为测试传递 test_config 来配置应用和数据库，而 不使用本地的开发配置
import os
import tempfile

import pytest
from pograph import create_app
from pograph.db import get_db,init_db

with open(os.path.join(os.path.dirname(__file__),'data.sql'),'rb') as f:
    _data_sql = f.read().decode('utf8')

@pytest.fixture
def app():
    db_fd,db_path=tempfile.mkstemp()
    app = create_app(
        {
            'TESTING':True,
            'DATABASE':db_path,
        }
    )

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()
@pytest.fixture
def runner(app):
    return app.test_cli_runner()