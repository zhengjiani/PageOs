# -*- encoding: utf-8 -*-
"""
@File    : users.py
@Time    : 2020/2/29 11:23 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import datetime
import json,uuid,jwt
from functools import wraps
from flask import jsonify, Blueprint, request,current_app
from werkzeug.security import generate_password_hash
from . import api
from ..models import db,User


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)
current_app.json_encoder = MyEncoder

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'msg':'Token is missing'}),401

        try:
            data = jwt.decode(token,current_app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'msg':'Token is invalid'}),401

        return f(current_user,*args,**kwargs)
    return decorated


@api.route('/user', methods=['GET'])
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


@api.route('/user/<public_id>', methods=['GET'])
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


@api.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(public_id=str(uuid.uuid4()), username=data['username'], password=hashed_password,admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "新用户创建成功"})

@api.route('/user/<public_id>', methods=['PUT'])
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



@api.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    token = jwt.encode(
            {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            current_app.config['SECRET_KEY'])
    user_data = {}
    user_data['username'] = user.username
    user_data['password'] = user.password
    user_data['token'] = token

    return jsonify(
        {"data": user_data,
         "meta": {"msg": "登录成功",
                  "status": 200}
         })