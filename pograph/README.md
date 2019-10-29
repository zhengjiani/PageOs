文件__init__.py

app = Flask(__name__, instance_relative_config=True) 创建 Flask 实例

instance_relative_config=True 告诉应用配置文件是相对于 instance folder 的相对路径。实例文件夹在 flaskr 包的外面，用于存放本地数据（例如配置密钥和数据库），不应当 提交到版本控制系统。
可以显式定义实例文件夹：
    
    app = Flask(__name__, instance_path='/path/to/instance/folder')
    # 提供的路径是绝对路径
    
运行应用

    $ export FLASK_APP=pograph
    $ export FLASK_ENV=development
    $ flask run
    
运行init-db命令

    $ flask init-db
    
视图是一个应用对请求进行响应的函数。 Flask 通过模型把进来的请求 URL 匹配到 对应的处理视图。视图返回数据， Flask 把数据变成出去的响应。 Flask 也可以反 过来，根据视图的名称和参数生成 URL 。

蓝图方式是把它们注册到蓝图，然后在工厂函数中 把蓝图注册到应用。

为了更好地管理文件，属于某个蓝图 的模板会被放在与蓝图同名的文件夹内。

除了 CSS ，其他类型的静态文件可以是 JavaScript 函数文件或者 logo 图片。它们 都放置于 flaskr/static 文件夹中，并使用 url_for('static', filename='...') 引用。

当你完成每个视图时，请保持开发服务器运行。当你保存修改后，请尝试在浏览器中 访问 URL ，并进行测试。

loop.last 是一个 Jinja for 循环 内部可用的特殊变量，它用于在每个 博客帖子后面显示一条线来分隔帖子，最后一个帖子除外

## 图可视化

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
    
## python动态获取图

        # -*- coding: utf-8 -*-
    # @Time    : 2019/6/4 17:59
    # @Author  : zhengjiani
    # @Software: PyCharm
    # @Blog    ：https://zhengjiani.github.io/
    import re
    from pograph.service.bokchoy_pages import litemll_page
    import collections
    import json
    #python动态创建图
    #获取结点
    def get_navgraph_nodes():
        # 获取A的所有子类
        sub_class_list = litemll_page.BasePage.__subclasses__()
        nodes = []
        for i in range(len(sub_class_list)):
            # 获取子类的类名
            class_name = sub_class_list[i].__name__
            nodes.append(class_name)
            # 找出复合页面对象类
            comp = sub_class_list[i].__subclasses__()
            for j in range(len(comp)):
                cls_name = comp[j].__name__
                nodes.append(cls_name)
        return nodes
    
    #获取边
    def get_page_methods(nodes):
        dic = {}
        # 获取每个页面对象的方法集合
        for i in range(len(nodes) - 1):
            keys = []
            keys.append(nodes[i])
            dic.fromkeys(keys)
            a = eval(nodes[i])
            listA = filter(lambda x: re.match(r'[^_]', x) and callable(getattr(a, x)), dir(a))
            del_items = ['handle_alert', 'is_browser_on_page', 'q', 'scroll_to_element', 'validate_url', 'visit',
                         'wait_for', 'wait_for_ajax', 'wait_for_element_absence', 'wait_for_element_invisibility',
                         'wait_for_element_presence', 'wait_for_element_visibility', 'wait_for_page', 'warning']
            ret = list(set(listA).difference(set(del_items)))
            dic[nodes[i]] = ret
        return dic
    def get_navgraph(dic):
        tree = lambda: collections.defaultdict(tree)
        dic_po = tree()
        dic_next = {
            'login' : 'HomePage',
            'goto_good' : 'GoodPage',
            'goto_promotion' : 'PromotionPage',
            'goto_stat' : 'StatPage',
            'goto_region' : 'RegionPage',
            'goto_user' : 'UserPage',
            'goto_sys' : 'SysPage',
            'logout': 'HomePage',
            'modify_password' : 'ModifyPasswordPage',
            'search_user': 'UserPage',
            'add_user' : 'UserPage',
            'get_user_data' : 'UserPage',
            'search_address' : 'AddressPage',
            'search_collect' : 'CollectPage',
            'search_footprint' : 'FootprintPage',
            'search_history' : 'HistoryPage',
            'search_feedback' : 'FeedbackPage',
            'search_region' : 'RegionPage',
            'add_brand' : 'BrandPage',
            'search_brand' : 'BrandPage',
            'search_category' : 'CategoryPage',
            'search_order' : 'OrderPage',
            'search_issue' : 'IssuePage',
            'search_keyword' : 'KeywordPage',
            'add_keyword' : 'KeywordPage',
            'add_good' : 'GoodPage',
            'search_good' : 'GoodPage',
            'search_comment' : 'CommentPage',
            'search_promotion' : 'PromotionPage',
            'add_ad' : 'AdPage',
            'add_topic' : 'TopicPage',
            'add_rule' : 'Groupon_rulePage',
            'search_rule': 'Groupon_rulePage',
            'search_activity' : 'Groupon_activityPage',
            'add_admin' : 'SysPage',
            'add_object' : 'OsPage'
    
        }
        dic_nav = {}
        for key,value_list in dic.items():
            for value in value_list:
                next_po = dic_next[value]
                dic_po[key][value]=next_po
                dic_nav[key]=next_po
        print(dic_nav)
        return json.dumps(dic_po)
    # g=DirectedGraph(dict1)
    # print(g.edges)
    def get_graph():
        dic = get_page_methods(get_navgraph_nodes())
        return get_navgraph(dic)
    if __name__ == '__main__':
        dic = get_page_methods(get_navgraph_nodes())
        print(get_navgraph(dic))
    # {"LoginPage": {"login": "HomePage"}, "HomePage": {"goto_good": "GoodPage", "goto_promotion": "PromotionPage", "goto_user": "UserPage", "goto_sys": "SysPage", "logout": "HomePage", "goto_stat": "StatPage", "goto_region": "RegionPage"}, "ModifyPasswordPage": {"modify_password": "ModifyPasswordPage"}, "UserPage": {"add_user": "UserPage", "get_user_data": "UserPage", "search_user": "UserPage"}, "AddressPage": {"search_address": "AddressPage"}, "CollectPage": {"search_collect": "CollectPage"}, "FootprintPage": {"search_footprint": "FootprintPage"}, "HistoryPage": {"search_history": "HistoryPage"}, "FeedbackPage": {"search_feedback": "FeedbackPage"}, "RegionPage": {"search_region": "RegionPage"}, "BrandPage": {"add_brand": "BrandPage", "search_brand": "BrandPage"}, "CategoryPage": {"search_category": "CategoryPage"}, "OrderPage": {"search_order": "OrderPage"}, "IssuePage": {"search_issue": "IssuePage"}, "KeywordPage": {"add_keyword": "KeywordPage", "search_keyword": "KeywordPage"}, "GoodPage": {"add_good": "GoodPage", "search_good": "GoodPage"}, "CreatePage": {"add_good": "GoodPage"}, "CommentPage": {"search_comment": "CommentPage"}, "PromotionPage": {"add_ad": "AdPage", "search_promotion": "PromotionPage"}, "TopicPage": {"add_topic": "TopicPage"}, "Groupon_rulePage": {"add_rule": "Groupon_rulePage", "search_rule": "Groupon_rulePage"}, "Groupon_activityPage": {"search_activity": "Groupon_activityPage"}, "SysPage": {"add_admin": "SysPage"}, "OsPage": {"add_object": "OsPage"}}