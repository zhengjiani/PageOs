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
            list_class = []
            class_info = inspect.getsource(page.FindOwnersPage).splitlines()
            for line in class_info:
                list_class.append(line.strip())
            list_class.remove(line.startswith('self'))
            return list_class
        else:
            raise ValueError('输入参数有误，请选择-get_po/get_po_param')


if __name__ == '__main__':
    p = PageObjectOperate()
    # print(p.get_po('get_po'))
    print(p.get_po('get_po_nav'))