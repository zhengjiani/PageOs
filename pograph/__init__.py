# -*- encoding: utf-8 -*-
"""
@File    : demo1.py
@Time    : 2019/10/24 9:02 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""

# __init__.py有两个作用：一是包含应用工厂，而是告诉py pograph应该视作一个包
import os
from flask import Flask

def create_app(test_config=None):
    # 创建和配置app
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path,'/Users/zhengjiani/PycharmProjects/PageOs_latest/pograph/pograph.sqlite'),
        UPLOAD_FOLDER='/Users/zhengjiani/PycharmProjects/PageOs_latest/pograph/service/pages'
    )

    # 在工厂中导入并调用这个函数
    from . import db
    db.init_app(app)
    # 导入并注册蓝图
    from pograph.route import auth
    app.register_blueprint(auth.bp)
    if test_config is None:
        # 不测试的时候加载实例配置
        app.config.from_pyfile('config.py',silent=True)
    else:
        # 加载测试配置
        app.config.from_mapping(test_config)
    from pograph.route import po
    app.register_blueprint(po.bp)
    app.add_url_rule('/',endpoint='index')
    return app
    #保证实例文件夹的存在
    try:
        os.mkdirs(app.instance_path)
    except OSError:
        pass