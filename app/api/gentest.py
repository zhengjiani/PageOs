# -*- encoding: utf-8 -*-
"""
@File    : gentest.py
@Time    : 2020/2/28 7:59 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import os
import sys

from flask import jsonify, send_from_directory
from . import api
from test_gen.generate_tree import Trans_tree


def get_key(dict,node,child):
    for key, val in dict.items():
        for k, v in val.items():
            if key == node and child == v:
                return k


@api.route('/transtree',methods=['GET'])
def trans_tree():
    pog_dic = {
        "AddNewPetPage": {
            "add_new_pet": "DetailPage"
        },
        "AddNewVisitPage": {
            "add_visit": "DetailPage"
        },
        "DetailPage": {
            "goto_add_pet": "AddNewPetPage",
            "goto_edit": "EditOwnerPage",
            "goto_edit_pet": "PetPage",
            "goto_pet": "PetPage",
            "goto_visit": "AddNewVisitPage"
        },
        "EditOwnerPage": {
            "edit_info": "DetailPage"
        },
        "FindPage": {
            "goto_detail_page": "DetailPage"
        },
        "HomePage": {
            "goto_Veter": "VeterPage",
            "goto_register": "RegisterPage",
            "goto_search": "FindPage"
        },
        "PetPage": {
            "edit_pet": "DetailPage"
        },
        "RegisterPage": {
            "regist_owner": "FindPage"
        },
        "VeterPage": {},
    }
    tree_dic,tree,po_hash = Trans_tree(pog_dic).tran_tree()
    tree.show()
    tree.save2file('tree.txt')
    tree_txt = "/Users/zhengjiani/PycharmProjects/PageOs_v0.1/tree.txt"
    paths = tree.paths_to_leaves()
    path = []
    for each in paths:
        path_lists = []
        for item in each:
            path_lists.append(str(item).replace(str(item),po_hash[item]))
        path.append(path_lists)
    methods = []
    for each in path:
        i = 0
        method = []
        if len(each) == 2:
            method.append(get_key(pog_dic, each[0], each[1]))
        else:
            while i < (len(each)-1):
                method.append(get_key(pog_dic, each[i], each[i+1]))
                i = i + 1
        methods.append(method)
    res_dict = {
        "data":
            {
                "tree_dic": tree.to_json(with_data=True),
                "tree_visual": tree_txt,
                "pathlists": path,
                "methods":methods
            },
        "meta":
            {
                "msg":"广度优先遍历树构建成功",
                "status": 200
            }
    }
    return jsonify(res_dict)


@api.route('/pathlists',methods=['GET'])
def get_paths():
    pathlists = [
        '<\HomePage:goto_search,FindPage:goto_detail_page,DetailPage>',
        '<\HomePage:goto_search,FindPage:goto_detail_page,DetailPage>',
        '<\HomePage:goto_search,FindPage:goto_detail_page,DetailPage:goto_edit_pet,PetPage:edit_pet(R1),DetailPage>',
        '<\HomePage:goto_search,FindPage:goto_detail_page,DetailPage:goto_visit,AddNewVisitPage:add_visit(R1),DetailPage>',
        '<\HomePage:goto_search,FindPage:goto_detail_page,DetailPage:goto_edit,EditOwnerPage:edit_info(R1),DetailPage>',
        '<\HomePage:goto_register,RegisterPage:regist_owner(R2),ErrorMsg>',
        '<\HomePage:goto_register,RegisterPage:regist_owner(R1),FindPage:goto_detail_page,DetailPage>',
        '<\HomePage:goto_Veter,VeterPage>'

    ]
    paths = []
    for i in pathlists:
        dic = {}
        dic['pathname'] = i
        paths.append(dic)
    res_dict = {
        "data":
        {
        "totalpage": 5,
        "pagenum": 4,
        "total":8,
        "paths": paths
        },
        "meta": {
            "msg": "获取成功",
            "status": 200
        }}
    return jsonify(res_dict)



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
