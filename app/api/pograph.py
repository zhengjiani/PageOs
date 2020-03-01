# -*- encoding: utf-8 -*-
"""
@File    : pograph.py
@Time    : 2020/2/28 7:53 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from flask import jsonify, request

from models import Page,db
from . import api
from bokchoy_pages import po_parse


@api.route('/pog/<int:page_id>',methods=['GET'])
def get_pog(page_id):
    page = Page.query.filter_by(id=page_id).first()
    page_data = {}
    page_data['pagename'] = page.pagename
    page_data['filepath'] = page.file_path
    pog_dic = po_parse.PageObjectOperate().get_po('get_po_dic')
    page_data['pog_dic'] = pog_dic
    pog_graph = "/Users/zhengjiani/PycharmProjects/PageOs_v0.1/graph.png"
    page_data['pog_graph'] = pog_graph
    return jsonify({'page':page_data,"msg":"页面对象图字典生成成功"})

@api.route('/pog', methods=['POST'])
def create_pog():
    data = request.get_json()
    new_page = Page(pagename=data['pagename'],file_path=data['filepath'])
    db.session.add(new_page)
    db.session.commit()
    return jsonify({"msg": "新页面对象文件创建成功"})

@api.route('/pog',methods=['GET'])
def get_all_pogs():
    pages = Page.query.all()
    output = []
    for page in pages:
        page_data = {}
        page_data['id'] = page.id
        page_data['pagename'] = page.pagename
        page_data['filepath'] = page.file_path
        output.append(page_data)
    return jsonify({'pages':output})

@api.route('/pog/<int:page_id>',methods=['DELETE'])
def delete_page(page_id):
    page = Page.query.filter_by(id=page_id).first()
    db.session.delete(page)
    db.session.commit()
    return jsonify({"msg": "新页面对象文件删除成功"})
