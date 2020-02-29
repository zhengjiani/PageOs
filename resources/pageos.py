# -*- encoding: utf-8 -*-
"""
@File    : pageos.py
@Time    : 2020/2/28 7:49 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from flask import jsonify, Blueprint, Response, request

pageos = Blueprint('pageos',__name__)

@pageos.route('/polists',methods=['GET'])
def get_po_files():
    res_dict = {
        "data":
            {
                "totalpage": 5,
                "pagenum": 4,
                "total": 8,
                "pos": [
                    {'poname':'PetClinic_page'},
                    {'poname':'pageKit_page'},
                    {'poname':'phoneix_page'}
                ]
            },
        "meta":{
            "msg": "获取成功",
            "status": 200
        }
    }
    return jsonify(res_dict)
