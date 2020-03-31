# -*- encoding: utf-8 -*-
"""
@File    : po_parse.py
@Time    : 2019/10/28 6:59 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from graphviz import Digraph
from bokchoy_pages import pet_page
class PageObjectOperate:
    # 获取po文件
    def get_po(self, name):
        # clsmembers = inspect.getmembers(sys.modules[page.__name__], inspect.isclass)
        # nodes = []
        # for class_name in clsmembers:
        #     if class_name[0] == 'BasePage':
        #         nodes.append(class_name[0])
        # dic = {}
        # dic_param = {}
        # for po in nodes:
        #     funmembers = inspect.getmembers(eval('page.{}'.format(po)), inspect.isfunction)
        #     edges = []
        #     for func in funmembers:
        #         if func[0] != '__init__':
        #             edges.append(func[0])
        #             params = inspect.getfullargspec(getattr(eval('page.{}'.format(po)), func[0]))
        #             list = params[0][1:]
        #             dic_param[func[0]] = list
        #             dic[po] = edges
        all_subclasses = []
        for subclass in pet_page.BasePage.__subclasses__():
            all_subclasses.append(subclass.__name__)
        # print(all_subclasses)
        cls = {}
        for page in all_subclasses:
            pmethods = ['q', 'is_browser_on_page', 'validate_url', 'visit', 'wait_for', 'wait_for_ajax',
                        'wait_for_element_absence', 'wait_for_element_invisibility',
                        'wait_for_element_presence', 'wait_for_element_visibility', 'wait_for_page',
                        'warning', 'handle_alert', 'scroll_to_element']
            methods = list(filter(lambda m: not m in pmethods and not m.startswith("__") \
                                            and not m.startswith("_") and not m.endswith("__") \
                                            and callable(getattr(eval('pet_page.'+page), m)), dir(eval('pet_page.'+page))))
            cls[page] = methods
        # print(cls)
        pog = {}
        for key, value in cls.items():
            pog[key] = {}
            for val in value:
                po = eval('pet_page.' + key + '.' + val).__doc__
                if po is not None:
                    pog[key][val] = po.split(':')[-1].strip()
                    # print(key + '->'+ po.split(':')[-1])
        # print(next_po)
        if name == 'get_po_dic':
            return pog
        elif name == 'get_po_nav':
            # # 合并图字典
            # # for po in nodes:
            # class_info = []
            # dic_next_po = {}
            # # list_class = re.split(r'[\n]\s*', inspect.getsource(eval('page.{}'.format(po))))
            # list_class = re.split(r'[\n]\s*', inspect.getsource(page.FindOwnersPage))
            # for line in list_class:
            #     if line.startswith('def') or line.startswith('return'):
            #         class_info.append(line)
            # for index, value in enumerate(class_info):
            #     if value.startswith('def') and class_info[index + 1].startswith('return'):
            #         dic_next_po[value.split(' ')[1].split('(')[0]] = class_info[index + 1].split(' ')[1].split('(')[0]
            # return dic_next_po
            # 图可视化
            dot = Digraph(comment='POG')
            for node in list(pog.keys()):
                dot.node(node)
            for k, v in pog.items():
                for k_val, v_val in v.items():
                    dot.edge(k, v_val, label=k_val)
            print(dot.source)
            dot.render('output/PetClinic.png', view=True)  # doctest: +SKIP
            return 'output/PetClinic.gv.pdf'
        else:
            raise ValueError('输入参数有误，请选择-get_po/get_po_param')

# 导航图可视化
def visual_graph():
    # 首先获取图字典
    # dic = {'LoginPage': {'login': 'HomePage'},
    #        'HomePage': {'goto_user': 'UserPage', 'logout': 'LoginPage'},
    #        'UserPage': {'add_user': 'UserListPage', 'remove_user': 'UserListPage', 'search_user': 'UserPage'}
    #        }
    dic = {'HomePage': {'goto_Veter': 'VeterPage', 'goto_register': 'RegisterPage', 'goto_search': 'FindPage'},
           'FindPage': {'goto_detail_page': 'DetailPage'}, 'RegisterPage': {'regist_owner': 'FindPage'},
           'DetailPage': {'goto_add_pet': 'AddNewPetPage', 'goto_edit': 'EditOwnerPage', 'goto_edit_pet': 'PetPage',
                          'goto_pet': 'PetPage', 'goto_visit': 'AddNewVisitPage'},
           'EditOwnerPage': {'edit_info': 'DetailPage'}, 'AddNewPetPage': {'add_new_pet': 'DetailPage'},
           'PetPage': {'edit_pet': 'DetailPage'}, 'AddNewVisitPage': {'add_visit': 'DetailPage'}, 'VeterPage': {}}

    dot = Digraph(comment='POG')
    for node in list(dic.keys()):
        dot.node(node)
    for k, v in dic.items():
        for k_val, v_val in v.items():
            dot.edge(k, v_val, label=k_val)
    print(dot.source)
    dot.render('output/PetClinic.png', view=True)  # doctest: +SKIP
    return 'output/PetClinic.gv.pdf'


if __name__ == '__main__':
    p = PageObjectOperate()
    print(p.get_po('get_po_dic'))
    print(p.get_po('get_po_nav'))
    # print(p.visual_graph())
    # visual_graph()