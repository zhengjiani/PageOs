# -*- encoding: utf-8 -*-
"""
@File    : pograph.py
@Time    : 2020/2/28 7:53 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from flask import jsonify, Blueprint, Response, request

pograph = Blueprint('pograph',__name__)

@pograph.route('/pogdict',methods=['GET'])
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

@pograph.route('/pog',methods=['GET'])
def get_pograph():
    img = "/Users/zhengjiani/PycharmProjects/PageOs_v0.1/test-output/petclinic_POG.png"
    return img

@pograph.route('/pog_after',methods=['GET'])
def get_pogafter():
    img = "/Users/zhengjiani/PycharmProjects/PageOs_v0.1/graph.png"
    return img
