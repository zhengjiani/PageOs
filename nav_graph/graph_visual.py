# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 18:00
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""实现读取字典，有向图可视化"""
from graphviz import Digraph
import string
import random
dic = {'LoginPage':{'login':'HomePage'},
       'HomePage':{'goto_user':'UserPage','logout':'LoginPage'},
       'UserPage':{'add_user':'UserListPage','remove_user':'UserListPage','search_user':'UserPage'}
       }

dot = Digraph(comment='Page Object Graph')
# for i in string.ascii_letters:
for k,v in dic.items():
       for k_val,v_val in v.items():
              dot.node(k)
              dot.node(v_val)
              dot.edge(k,v_val,label=k_val)
print(dot.source)
dot.render('test-output/round-table.gv', view=True)  # doctest: +SKIP
'test-output/round-table.gv.pdf'