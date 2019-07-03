import re
from bokchoy_pages import litemll_page
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
    get_navgraph(dic)

