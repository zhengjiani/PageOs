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
from flask import jsonify, Blueprint, request, current_app, make_response
from werkzeug.security import generate_password_hash
from . import api
from ..code import ResponseCode, ResponseMessage
from ..models import db,User
from ..response import ResMsg
from ..util import route
from .. import dao


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

@route(api,'/user', methods=['GET'])
def get_all_users():
    res = ResMsg()
    res_list = dao.get_users()
    res.update(code=ResponseCode.SUCCESS,data=res_list)
    return res.data


@route(api,'/user/<public_id>', methods=['GET'])
def get_one_user(public_id):
    res = ResMsg()
    output = dao.get_user(public_id)
    res.update(code=ResponseCode.SUCCESS, data=output)
    return res.data



@route(api,'/user', methods=['POST'])
def create_user():
    res = ResMsg()
    req = request.get_json()
    hashed_password = generate_password_hash(req['password'], method='sha256')
    data = {
        'public_id': str(uuid.uuid4()),
        'username': req['username'],
        'password': hashed_password,
        'admin': False
    }
    output = dao.add_user(data)
    if output is 'error':
        res.update(code=ResponseCode.FAIL, data=output, msg=ResponseMessage.FAIL)
    else:
        res.update(code=ResponseCode.SUCCESS, data=output)
    return res.data


@route(api,'/user/<public_id>', methods=['PUT'])
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



@route(api,'/login',methods=['POST'])
def login():
    res = ResMsg()
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    token = jwt.encode(
            {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            current_app.config['SECRET_KEY'])
    user_data = {}
    user_data['username'] = user.username
    user_data['password'] = user.password
    user_data['token'] = token

    res.update(code=ResponseCode.SUCCESS,data=user_data)

