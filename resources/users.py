# -*- encoding: utf-8 -*-
"""
@File    : users.py
@Time    : 2020/2/29 11:23 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""

import os
from functools import wraps

from flask import jsonify, Blueprint, Response, request, send_from_directory
from jwt import jwt


users = Blueprint('users',__name__)

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