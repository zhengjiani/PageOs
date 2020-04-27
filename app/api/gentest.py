# -*- encoding: utf-8 -*-
"""
@File    : gentest.py
@Time    : 2020/2/28 7:59 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import ast
import os
import sys

from flask import jsonify, send_from_directory, request
from . import api
from gen_test.generate_tree import Trans_tree
from .. import dao
from ..code import ResponseCode
from ..response import ResMsg
from ..util import route
from gen_test.gen_testcase import gen_test


def get_key(dict,node,child):
    for key, val in dict.items():
        for k, v in val.items():
            if key == node and child == v:
                return k


@route(api,'/transtree',methods=['GET','POST'])
def trans_tree():
    """返回页面对象迁移树"""
    res = ResMsg()
    data = request.get_json()
    result = dao.get_dict_by_name(data["pagename"])
    pog_dic = ast.literal_eval(result['pog'])
    print(pog_dic)
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
    pathList = []
    res_pet = {
                "pagename": "PetClinic_page",
                "tree_dic": tree.to_json(with_data=True),
                "tree_visual": tree_txt,
                "pathlists": path,
                "methods":methods

    }
    pathList.append(res_pet)
    res_dict = {
        "paths":pathList
    }
    res.update(code=ResponseCode.SUCCESS,data=res_dict,msg="页面对象迁移树转换成功")
    return res.data


@route(api,'/pathlists',methods=['GET'])
def get_paths():
    """返回路径"""
    res = ResMsg()
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
        "totalpage": 5,
        "pagenum": 4,
        "total":8,
        "paths": paths
        }
    res.update(code=ResponseCode.SUCCESS, data=res_dict)
    return res.data



@route(api,'/makedata',methods=['GET','POST'])
def make_data():
    """生成模拟数据"""
    res = ResMsg()
    res_dict = {'first_name': 'Isabella', 'last_name': 'Holmes', 'address': '3119 Alvarez Overpass Suite 542',
                'city': 'bury', 'telephone': '751-416-7438x05474'}
    res.update(code=ResponseCode.SUCCESS, data=res_dict)
    return res.data

@route(api,'/testfile/<filename>',methods=['GET'])
def get_test_file(filename):
    """获取文件路径及文件"""
    directory = os.getcwd()
    file_path=os.path.join(directory,'bokchoy_pages')
    return send_from_directory(file_path, filename, as_attachment=True)

@route(api,'/gentests',methods=['POST'])
def get_testcases():
    """根据测试路径集生成测试用例，获取测试用例"""
    res = ResMsg()
    req = request.get_json()
    pathlists = req["pathlists"]
    print(pathlists)
    gen_test().generate(pathlists)
    file = '/Users/zhengjiani/PycharmProjects/PageOs_v0.1/gen_test/path_test.py'
    if os.path.exists(file):
        res.update(code=ResponseCode.SUCCESS, data={'file_path':file}, msg="测试用例文件生成成功")
    return res.data

