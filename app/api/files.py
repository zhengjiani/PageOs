# -*- encoding: utf-8 -*-
"""
@File    : files.py
@Time    : 2020/2/29 11:26 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import os

from flask import jsonify, request, send_from_directory, current_app, make_response
from werkzeug.utils import secure_filename
from . import api
from ..util import route

@route(api,'/upload',methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        print(file.filename)
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return {"status": 201, "msg": "upload success"}


@route(api,'/download/<filename>',methods=['GET'])
def download_file(filename):
    directory = os.getcwd()
    print(directory)
    path = os.path.join(directory,'download/MySite.py')
    # response = send_from_directory(path,filename,as_attachment=True)
    f_content = open(path,'r',encoding='UTF-8').read()
    # print(response)
    return {"code": 0, "msg": "页面对象文件下载成功", "data":f_content}

@route(api,'/testsuite/<filename>',methods=['GET'])
def testsuite(filename):
    directory = os.getcwd()
    path = os.path.join(directory,'gen_test/path_test.py')
    f_content = open(path,'r',encoding='UTF-8').read()
    return {"code": 0, "msg": "测试套件预览成功", "data":f_content}
