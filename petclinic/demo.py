# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 22:14
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
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
# 合并字典
# z_dic = dic_graph.update(dic_params)
# print(dic_graph)
for k,val in dic_graph.items():
    current_page = k
    for v in val:
        func_name = v
        for kk,vv in dic_params.items():
            if kk == v:
                params = vv
                print(current_page,func_name,params)