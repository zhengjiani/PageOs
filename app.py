# -*- encoding: utf-8 -*-
"""
@File    : app.py
@Time    : 2020/1/4 1:07 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from flask import Flask, jsonify
import yaml
from utils.response import ResMsg
from utils.core import JSONEncoder, db
from po_parse import PageObjectOperate

app = Flask(__name__)

with open("msg.yaml", encoding="utf-8") as f:
    msg_conf = yaml.safe_load(f)
app.config.update(msg_conf)
# 返回json格式转换
app.json_encoder = JSONEncoder

USERNAME = 'root' # 用户名
PASSWORD = 'mad123' # 密码
HOST = '127.0.0.1' # 数据库地址
PORT = '3306' # 端口
DATABASE = 'test' #数据库名
database_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOST, PORT, DATABASE
)
# 添加数据库配置文件到flask app中
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
# 注册数据库连接
db.app = app
db.init_app(app)

@app.route("/",methods=["GET"])
def test():
    res = ResMsg()
    test_dict = dict(name="zhang",age=18)
    res.update(data=test_dict)
    # data=dict(code=ResponseCode.SUCCESS,
    #           msg=ResponseMessage.SUCCESS,
    #           data=test_dict)
    return jsonify(res.data)

@app.route("/po",methods=['GET'])
def get_po():
    """
    获取类名
    :return:
    """
    res = ResMsg()
    p = PageObjectOperate()
    graph_dict = p.get_po('get_po')
    res.update(data=graph_dict)
    return jsonify(res.data)

@app.route("/po_param",methods=['GET'])
def get_po_param():
    """
    获取类参数
    :return:
    """
    res = ResMsg()
    p = PageObjectOperate()
    graph_dict = p.get_po('get_po_param')
    res.update(data=graph_dict)
    return jsonify(res.data)

@app.route("/po_nav",methods=['GET'])
def get_po_nav():
    """
    获取类参数
    :return:
    """
    res = ResMsg()
    p = PageObjectOperate()
    graph_dict = p.get_po('get_po_nav')
    res.update(data=graph_dict)
    return jsonify(res.data)

if __name__ == '__main__':
    app.run(debug=True)

