# -*- encoding: utf-8 -*-
"""
@File    : po_parse.py
@Time    : 2019/10/28 6:59 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import inspect
import sys
import re
from graphviz import Digraph
import string
import random
from pograph.service.pages import page
class PageObjectOperate:
    # 获取po文件
    def get_po(self,name):
        clsmembers = inspect.getmembers(sys.modules[page.__name__], inspect.isclass)
        nodes = []
        for class_name in clsmembers:
            if class_name[0].endswith('Page'):
                nodes.append(class_name[0])
        dic = {}
        dic_param = {}
        for po in nodes:
            funmembers = inspect.getmembers(eval('page.{}'.format(po)), inspect.isfunction)
            edges = []
            for func in funmembers:
                if func[0] != '__init__':
                    edges.append(func[0])
                    params = inspect.getfullargspec(getattr(eval('page.{}'.format(po)), func[0]))
                    list = params[0][1:]
                    dic_param[func[0]] = list
                    dic[po] = edges

        if name == 'get_po':
            return dic
        elif name == 'get_po_param':
            return dic_param
        elif name == 'get_po_nav':
            # 合并图字典
            # for po in nodes:
            class_info = []
            dic_next_po = {}
            # list_class = re.split(r'[\n]\s*', inspect.getsource(eval('page.{}'.format(po))))
            list_class = re.split(r'[\n]\s*', inspect.getsource(page.FindOwnersPage))
            for line in list_class:
                if line.startswith('def') or line.startswith('return'):
                    class_info.append(line)
            for index, value in enumerate(class_info):
                if value.startswith('def') and class_info[index + 1].startswith('return'):
                    dic_next_po[value.split(' ')[1].split('(')[0]] = class_info[index + 1].split(' ')[1].split('(')[0]
            return dic_next_po
        else:
            raise ValueError('输入参数有误，请选择-get_po/get_po_param')

    # 导航图可视化
    def visual_graph(self):
        # 首先获取图字典
        dic = {'LoginPage': {'login': 'HomePage'},
               'HomePage': {'goto_user': 'UserPage', 'logout': 'LoginPage'},
               'UserPage': {'add_user': 'UserListPage', 'remove_user': 'UserListPage', 'search_user': 'UserPage'}
               }

        dot = Digraph(comment='Page Object Graph')
        # for i in string.ascii_letters:
        for k, v in dic.items():
            for k_val, v_val in v.items():
                dot.node(k)
                dot.node(v_val)
                dot.edge(k, v_val, label=k_val)
        print(dot.source)
        dot.render('test-output/round-table.gv', view=True)  # doctest: +SKIP
        return 'test-output/round-table.gv.pdf'


if __name__ == '__main__':
    p = PageObjectOperate()
    # print(p.get_po('get_po'))
    # print(p.get_po('get_po_nav'))
    print(p.visual_graph())