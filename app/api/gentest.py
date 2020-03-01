# -*- encoding: utf-8 -*-
"""
@File    : gentest.py
@Time    : 2020/2/28 7:59 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import os

from flask import jsonify, send_from_directory
from . import api


@api.route('/pathlists',methods=['GET'])
def get_paths():
    res_dict = {
        "data":
        {
        "totalpage": 5,
        "pagenum": 4,
        "total":8,
        "paths": [
            {
                'pathname':'<\HomePage:goto_search,FindPage:goto_detail_page,DetailPage>'
            },
            {
                'pathname': '<\HomePage:goto_search,FindPage:goto_detail_page,DetailPage>'
            },
            {
                'pathname': '<\HomePage:goto_search,FindPage:goto_detail_page,DetailPage:goto_edit_pet,PetPage:edit_pet(R1),DetailPage>'
            },
            {
                'pathname': '<\HomePage:goto_search,FindPage:goto_detail_page,DetailPage:goto_visit,AddNewVisitPage:add_visit(R1),DetailPage>'
            },
            {
                'pathname': '<\HomePage:goto_search,FindPage:goto_detail_page,DetailPage:goto_edit,EditOwnerPage:edit_info(R1),DetailPage>'
            },
            {
                'pathname': '<\HomePage:goto_register,RegisterPage:regist_owner(R2),ErrorMsg>'
            },
            {
                'pathname': '<\HomePage:goto_register,RegisterPage:regist_owner(R1),FindPage:goto_detail_page,DetailPage>'
            },
            {
                'pathname': '<\HomePage:goto_Veter,VeterPage>'
            }
        ]
        },
        "meta": {
            "msg": "获取成功",
            "status": 200
        }}
    return jsonify(res_dict)

@api.route('/pagefiles',methods=['POST'])
def add_pos():
    pass

@api.route('/makedata',methods=['GET','POST'])
def make_data():
    res_dict = {'first_name': 'Isabella', 'last_name': 'Holmes', 'address': '3119 Alvarez Overpass Suite 542',
                'city': 'bury', 'telephone': '751-416-7438x05474'}
    return jsonify({'data':res_dict})

@api.route('/testfile/<filename>',methods=['GET'])
def get_test_file(filename):
    directory = os.getcwd()
    file_path=os.path.join(directory,'bokchoy_pages')
    return send_from_directory(file_path, filename, as_attachment=True)
