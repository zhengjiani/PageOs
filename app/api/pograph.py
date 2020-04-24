# -*- encoding: utf-8 -*-
"""
@File    : pograph.py
@Time    : 2020/2/28 7:53 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from flask import jsonify, request

from app.models import Page,db
from . import api
from bokchoy_pages import po_parse
from .. import dao
from ..code import ResponseCode
from ..response import ResMsg
from ..util import route


@route(api,'/pog/<int:page_id>',methods=['GET'])
def get_pog(page_id):
    res = ResMsg()
    page = dao.get_pog_by_id(page_id)
    page_data = {}
    page_data['pagename'] = page["pagename"]
    page_data['filepath'] = page["file_path"]
    pog_dic = po_parse.PageObjectOperate().get_po('get_po_dic',page["pagename"])
    page_data['pog_dic'] = pog_dic
    pog_graph = "/Users/zhengjiani/PycharmProjects/PageOs_v0.1/graph.png"
    page_data['pog_graph'] = pog_graph
    res.update(code=ResponseCode.SUCCESS,data=page_data,msg="Web应用导航图生成成功")
    return res.data

@route(api,'/pog',methods=['GET','POST'])
def get_pog_by_name():
    res = ResMsg()
    data = request.get_json()
    page = dao.get_pog_by_name(data['pagename'])
    page_data = {}
    page_data['pagename'] = page["pagename"]
    page_data['filepath'] = page["file_path"]
    pog_dic = po_parse.PageObjectOperate().get_po('get_po_dic', data['pagename'])
    print(pog_dic)
    page_data['pog_dic'] = pog_dic
    pog_graph = page["graph_path"]
    page_data['pog_graph'] = pog_graph
    res.update(code=ResponseCode.SUCCESS, data=page_data, msg="Web应用导航图生成成功")
    return res.data


@route(api,'/pog', methods=['POST'])
def create_pog():
    data = request.get_json()
    new_page = Page(pagename=data['pagename'],file_path=data['filepath'])
    db.session.add(new_page)
    db.session.commit()
    return jsonify({"msg": "新页面对象文件创建成功"})

@route(api,'/pog',methods=['GET'])
def get_all_pogs():
    res = ResMsg()
    pages = Page.query.all()
    output = []
    for page in pages:
        page_data = {}
        page_data['id'] = page.id
        page_data['pagename'] = page.pagename
        page_data['filepath'] = page.file_path
        output.append(page_data)
    res.update(code=ResponseCode.SUCCESS,data=output)

@route(api,'/pog/<int:page_id>',methods=['DELETE'])
def delete_page(page_id):
    page = Page.query.filter_by(id=page_id).first()
    db.session.delete(page)
    db.session.commit()
    return jsonify({"msg": "新页面对象文件删除成功"})
