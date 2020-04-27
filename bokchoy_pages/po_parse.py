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
from bokchoy_pages.phoenix import phoenix_page
from bokchoy_pages.pageKit.po import pageKit_po_page
class PageObjectOperate:
    # 获取po文件
    def get_po(self, cmd_name, page_name):
        all_subclasses = []
        dic = {
            'PetClinic_page': pet_page,
            'pageKit_page': pageKit_po_page,
            'phoenix_page': phoenix_page
        }
        for subclass in dic[page_name].BasePage.__subclasses__():
            all_subclasses.append(subclass.__name__)
        # print(all_subclasses)
        cls = {}
        page_dic = {
            'PetClinic_page': 'pet_page.',
            'pageKit_page': 'pageKit_po_page.',
            'phoenix_page': 'phoenix_page.'
        }
        for page in all_subclasses:
            pmethods = ['q', 'is_browser_on_page', 'validate_url', 'visit', 'wait_for', 'wait_for_ajax',
                        'wait_for_element_absence', 'wait_for_element_invisibility',
                        'wait_for_element_presence', 'wait_for_element_visibility', 'wait_for_page',
                        'warning', 'handle_alert', 'scroll_to_element']
            methods = list(filter(lambda m: not m in pmethods and not m.startswith("__") \
                                            and not m.startswith("_") and not m.endswith("__") \
                                            and callable(getattr(eval(page_dic[page_name]+page), m)), dir(eval(page_dic[page_name]+page))))
            cls[page] = methods
        # print(cls)
        pog = {}
        for key, value in cls.items():
            pog[key] = {}
            for val in value:
                po = eval(page_dic[page_name] + key + '.' + val).__doc__
                if po is not None:
                    pog[key][val] = po.split(':')[-1].strip()
                    # print(key + '->'+ po.split(':')[-1])
        # print(next_po)
        if cmd_name == 'get_po_dic':
            return pog
        elif cmd_name == 'get_po_nav':
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
    # p = PageObjectOperate()
    # print(p.get_po('get_po_dic'))
    p = PageObjectOperate()
    print(p.get_po('get_po_dic','phoenix_page'))
    # print(p.get_po('get_po_nav'))
    # print(p.visual_graph())
    # visual_graph()