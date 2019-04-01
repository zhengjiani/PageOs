import re
from pro_one.util import DirectWeightGraph
from pro_one import litemll_page
from pro_one.litemll_page import LoginPage,HomePage,ModifyPasswordPage,UserPage,AddressPage,CollectPage,FootprintPage,HistoryPage,\
                                FeedbackPage,RegionPage,BrandPage,CategoryPage,OrderPage,IssuePage,KeywordPage,GoodPage,CreatePage,\
                                CommentPage,PromotionPage,TopicPage,Groupon_rulePage,Groupon_activityPage,SysPage,OsPage,StatPage
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
            'login': 'HomePage',
            'other': 'ErrorPage',
            'goto_good':'GoodPage',
            'goto_other':'OtherPage'
    }
    for key,value_list in dic.items():
        for value in value_list:
            next_po = dic_next[value]
            print(next_po)
            dic_po[key][value]=next_po
    return json.dumps(dic_po)
# g=DirectedGraph(dict1)
# print(g.edges)
#广度优先遍历
def bfs_traverse(graph, start):
    visited, queue = set(), [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for nextNode in graph[node]:
                if nextNode not in visited:
                    queue.append(nextNode)
    return visited

if __name__ == '__main__':
     nodes = get_navgraph_nodes()
     print(get_page_methods(nodes))
     dic = get_page_methods(get_navgraph_nodes())
     print(get_navgraph({'LoginPage': ['login','other'],'HomePage':['goto_good','goto_other']}))