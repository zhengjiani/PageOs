# -*- encoding: utf-8 -*-
"""
@File    : app.py
@Time    : 2020/1/4 1:07 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import json
import os

from flask import Flask, request, jsonify, send_file,send_from_directory
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
from flask_cors import *
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)

CORS(app, supports_credentials=True)
USERNAME = 'root'  # 用户名
PASSWORD = 'ZhengJiaNi@88'  # 密码
HOST = 'localhost'  # 数据库地址
PORT = '3306'  # 端口
DATABASE = 'flask_pos'  # 数据库名
database_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOST, PORT, DATABASE
)
# 添加数据库配置文件到flask app中
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)
app.json_encoder = MyEncoder

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password = db.Column(db.String(128))
    public_id = db.Column(db.String(50), unique=True)
    admin = db.Column(db.Boolean)



def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'msg':'Token is missing'}),401

        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'msg':'Token is invalid'}),401

        return f(current_user,*args,**kwargs)
    return decorated


@app.route('/user', methods=['GET'])
def get_all_users():

    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['username'] = user.username
        user_data['password'] = user.password
        user_data['admin'] = user.admin

        output.append(user_data)

    return jsonify({'users': output})


@app.route('/user/<public_id>', methods=['GET'])
def get_one_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'msg': 'No user found!'})

    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['username'] = user.username
    user_data['password'] = user.password
    user_data['admin'] = user.admin

    return jsonify({'user': user_data})


@app.route('/user', methods=['POST'])
def create_user():

    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(public_id=str(uuid.uuid4()), username=data['username'], password=hashed_password,admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "新用户创建成功"})

@app.route('/user/<public_id>', methods=['PUT'])
def promote_user(public_id):
    """
    提升用户权限
    :param current_user:
    :param public_id:
    :return:
    """
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'msg': 'No user found'})

    user.admin = False
    db.session.commit()

    return jsonify({'msg':'用户权限提升'})



@app.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    token = jwt.encode(
            {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config['SECRET_KEY'])
    user_data = {}
    user_data['username'] = user.username
    user_data['password'] = user.password
    user_data['token'] = token

    return jsonify(
        {"data": user_data,
         "meta": {"msg": "登录成功",
                  "status": 200}
         })

@app.route('/menus',methods=['GET'])
def get_menus():
    res_dict ={
            "data": [
                {
                    "id": 101,
                    "authName": "页面对象",
                    "path": None,
                    "children": [
                        {
                            "id": 104,
                            "authName": "页面对象自动生成",
                            "path": "auto",
                            "children": []
                        },
                        {
                            "id": 105,
                            "authName": "页面对象手动编写",
                            "path": "manual",
                            "children": []
                        },
                        {
                            "id": 106,
                            "authName": "页面对象文件管理",
                            "path": "pageos",
                            "children": []
                        }
                    ]
                },
                {
                    "id": 102,
                    "authName": "Web应用导航图",
                    "path": None,
                    "children": [
                        {
                            "id": 107,
                            "authName": "Web应用导航图生成",
                            "path": "graph",
                            "children": []
                        },
                        {
                            "id": 108,
                            "authName": "Web应用导航图管理",
                            "path": "graphli",
                            "children": []
                        }
                    ]
                },
                {
                    "id": 103,
                    "authName": "Web测试用例生成",
                    "path": None,
                    "children": [
                        {
                            "id": 109,
                            "authName": "测试路径提取",
                            "path": "pathsGraph",
                            "children": []
                        },
                        {
                            "id": 110,
                            "authName": "测试用例生成",
                            "path": "testCase",
                            "children": []
                        }
                    ]
                }
                ],
            "meta": {
                "msg": "获取菜单列表成功",
                "status": 200
            }
        }
    return jsonify(res_dict)

@app.route('/upload',methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        print(file.filename)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return {"status": 201, "msg": "upload success"}

@app.route('/pogdict',methods=['GET'])
def get_pog():
    dic = {'HomePage': {'goto_Veter': 'VeterPage', 'goto_register': 'RegisterPage',
                                      'goto_search': 'FindPage'}, 'FindPage': {'goto_detail_page': 'DetailPage'},
                         'RegisterPage': {'regist_owner': 'FindPage'},
                         'DetailPage': {'goto_add_pet': 'AddNewPetPage', 'goto_edit': 'EditOwnerPage',
                                        'goto_edit_pet': 'PetPage', 'goto_pet': 'PetPage',
                                        'goto_visit': 'AddNewVisitPage'}, 'EditOwnerPage': {'edit_info': 'DetailPage'},
                         'AddNewPetPage': {'add_new_pet': 'DetailPage'}, 'PetPage': {'edit_pet': 'DetailPage'},
                         'AddNewVisitPage': {'add_visit': 'DetailPage'}, 'VeterPage': {}}
    return jsonify({'data':dic})

@app.route('/pog',methods=['GET'])
def get_pograph():
    img = "/Users/zhengjiani/PycharmProjects/PageOs_v0.1/test-output/petclinic_POG.png"
    return img

@app.route('/download/<filename>',methods=['GET'])
def download_file(filename):
    directory = os.getcwd()
    return send_from_directory(directory,filename,as_attachment=True)

@app.route('/pog_after',methods=['GRT'])
def get_pogafter():
    img = "/Users/zhengjiani/PycharmProjects/PageOs_v0.1/graph.png"
    return img
if __name__ == '__main__':
    app.run(debug=True)
