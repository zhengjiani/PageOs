# -*- encoding: utf-8 -*-
"""
@File    : files.py
@Time    : 2020/2/29 11:26 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import os

from flask import jsonify,request, send_from_directory,current_app
from werkzeug.utils import secure_filename
from . import api

@api.route('/upload',methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        print(file.filename)
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return {"status": 201, "msg": "upload success"}

@api.route('/download/<filename>',methods=['GET'])
def download_file(filename):
    directory = os.getcwd()
    return send_from_directory(directory,filename,as_attachment=True)
