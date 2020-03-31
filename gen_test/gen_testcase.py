# -*- encoding: utf-8 -*-
"""
@File    : gen_testcase.py
@Time    : 2020/3/30 7:28 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from jinja2 import Environment,  FileSystemLoader

env = Environment(loader=FileSystemLoader("./templates"))
template = env.get_template("testcase.j2")

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
path = []
methods = []
pages = set()
for item in pathlists:
    path.append(item[2:][:-1].split(','))
for item in path:
    method = {}
    for i in item:
        if ':' in i:
            pages.add(i.split(':')[0])
            method[i.split(':')[0]]= i.split(':')[1]
        if i.endswith('Page'):
            pages.add(i)
    methods.append(method)


content = template.render(pathlists=path,pages = list(pages),methods=methods,type=type)

with open('./path_test.py','w') as fp:
    fp.write(content)