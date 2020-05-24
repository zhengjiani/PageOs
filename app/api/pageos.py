# -*- encoding: utf-8 -*-
"""
@File    : pageos.py
@Time    : 2020/2/28 7:49 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from flask import jsonify, Blueprint, Response, request
from . import api
from ..code import ResponseCode
from ..response import ResMsg
from ..util import route

@route(api,'/polists',methods=['GET'])
def get_po_files():
    res = ResMsg()
    res_dict = {
                "totalpage": 5,
                "pagenum": 4,
                "total": 8,
                "pos": [
                    {'poname':'PetClinic_page',
                     'file_path':'/Users/zhengjiani/PycharmProjects/PageOs_v0.1/bokchoy_pages/pet_page.py',
                     'graph_path':'http://localhost:5000/static/PetClinic.png'
                     },
                    {'poname':'pageKit_page',
                     'file_path':'/Users/zhengjiani/PycharmProjects/PageOs_v0.1/bokchoy_pages/pageKit/po/pageKit_po_page.py',
                     'graph_path':'http://localhost:5000/static/pageKit.png'
                     },
                    {'poname':'phoneix_page',
                     'file_path':'/Users/zhengjiani/PycharmProjects/PageOs_v0.1/bokchoy_pages/phoenix/phoenix_page.py',
                     'graph_path':'http://localhost:5000/static/phonenix.png'
                     }
                ]
        }

    res.update(code=ResponseCode.SUCCESS,data=res_dict)
    return res.data
