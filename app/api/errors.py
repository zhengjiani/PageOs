# -*- encoding: utf-8 -*-
"""
@File    : errors.py
@Time    : 2020/3/12 9:17 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from flask import request, jsonify, render_template
from . import api

@api.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and \
        not request.accept_mimetypes.accept_html:
        response = jsonify({'error':'not found'})
        response.status_code = 404
        return response
    return render_template('404.html'),404

@api.app_errorhandler(403)
def forbidden(message):
    response = jsonify({'error':'forbidden','message':message})
    response.status_code = 403
    return response
