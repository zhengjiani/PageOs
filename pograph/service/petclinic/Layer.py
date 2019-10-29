# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 17:20
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
自动生成testcase的模板
"""
from jinja2 import Template
from jinja2 import Environment,PackageLoader

env = Environment(loader=PackageLoader('petclinic'))
template = env.get_template('testcase.j2')

dic_graph = {'AddOwnerPage': ['add_owner'],
               'AddPetPage': ['add_pet'],
               'AddVisitPage': ['add_date'],
               'EditOwnerPage': ['edit_address', 'edit_city', 'edit_firstname', 'edit_lastname', 'edit_telephone'],
               'EditPetPage': ['edit_birth_date', 'edit_pet_name'],
               'FindOwnersPage': ['check_invalid_lastname_message', 'find_lastname', 'find_list'],
               'OwnersListPage': ['list_detail']}
dic_params = {'add_owner': ['firstName', 'lastName', 'address', 'city', 'telephone'],
              'add_pet': ['name', 'birthDate'],
              'add_date': ['date', 'description'],
              'edit_address': ['address'],
              'edit_city': ['city'],
              'edit_firstname': ['firstName'],
              'edit_lastname': ['lastName'],
              'edit_telephone': ['telephone'],
              'edit_birth_date': ['birthDate'],
              'edit_pet_name': ['name'], 'check_invalid_lastname_message': [],
              'find_lastname': ['lastname'], 'find_list': [], 'list_detail': []
              }

# for k,val in dic_graph.items():
#     current_page = k
#     for v in val:
#         func_name = v
#         for kk,vv in dic_params.items():
#             if kk == v:
#                 params = vv
dic = {
        # 'cls_name':'PetTest',
        # 'tc_name': 'add_owner',
        # 'url': 'http://localhost:8080/owners/new',
        # 'current_page': current_page,
        # 'func_name':func_name,
        # 'params': tuple(params)
        'dic_graph':dic_graph,
        'dic_params':dic_params
        }
content = template.render(dic)
print(content)
# with open('./test_add_owner.py','w') as fp:
#     fp.write(content)

