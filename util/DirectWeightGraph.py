from treelib import Node,Tree
tree = Tree()
class Node(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_name(obj):
        if isinstance(obj, Node):
            return obj.name
        elif isinstance(obj, str):
            return obj
        return ''

    def __eq__(self, obj):
        return self.name == self.get_name(obj)

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __ne__(self, obj):
        return self.name != self.get_name(obj)

    def __lt__(self, obj):
        return self.name < self.get_name(obj)

    def __le__(self, obj):
        return self.name <= self.get_name(obj)

    def __gt__(self, obj):
        return self.name > self.get_name(obj)

    def __ge__(self, obj):
        return self.name >= self.get_name(obj)

    def __bool__(self):
        return self.name

class Weight(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_name(obj):
        if isinstance(obj, Node):
            return obj.name
        elif isinstance(obj, str):
            return obj
        return ''

    def __eq__(self, obj):
        return self.name == self.get_name(obj)

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __ne__(self, obj):
        return self.name != self.get_name(obj)

    def __lt__(self, obj):
        return self.name < self.get_name(obj)

    def __le__(self, obj):
        return self.name <= self.get_name(obj)

    def __gt__(self, obj):
        return self.name > self.get_name(obj)

    def __ge__(self, obj):
        return self.name >= self.get_name(obj)

    def __bool__(self):
        return self.name
class DirectedWeightedEdge(object):
    def __init__(self, node_from, node_to,weight):
        self.nf = node_from
        self.nt = node_to
        self.wt = weight
    def __eq__(self, obj):
        if isinstance(obj, DirectedWeightedEdge):
            return obj.nf == self.nf and obj.nt == self.nt and obj.wt == self.wt
        return False

    def __repr__(self):
        return '({0} ->{1} {2})'.format(self.nf, self.nt,self.wt)
class DirectedWeightGraph(object):
    def __init__(self, load_dict={}):
        self.nodes = []
        self.edges = []
        self.weights = []
        self.adjmt = {}
        if load_dict and type(load_dict) == dict:
            for v,method in load_dict.items():
                node_from = self.add_node(v)
                self.adjmt[node_from]={}
                for w,n in method.items():
                    node_to = self.add_node(n)
                    weight = self.add_weight(w)
                    self.adjmt[node_from][weight]=node_to
                    self.add_edge(v,n,w)

                # self.adjmt[node_from][method] = []
                # for w in self.adjmt[node_from].values():
                #     for n in self.adjmt[node_from].values():
                #         node_to = self.add_node(n)
                #         self.adjmt[node_from].append(node_to)
                #         self.add_edge(v, n, k)

    def add_node(self, node_name):
        try:
            return self.nodes[self.nodes.index(node_name)]
        except ValueError:
            node = Node(node_name)
            self.nodes.append(node)
            return node
    def add_weight(self, weight_name):
        try:
            return self.weights[self.weights.index(weight_name)]
        except ValueError:
            weight = Weight(weight_name)
            self.weights.append(weight)
            return weight
    def add_edge(self, node_name_from, node_name_to,weight):
        try:
            node_from = self.nodes[self.nodes.index(node_name_from)]
            node_to = self.nodes[self.nodes.index(node_name_to)]
            edge_weight = self.weights[self.weights.index(weight)]
            self.edges.append(DirectedWeightedEdge(node_from, node_to,edge_weight))
        except ValueError:
            pass
# find path from start to end using recursion with backtracking
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if (start == end):
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            return newpath
    return None

# find all path无向图
def find_all_path(graph, start, end, path=[]):
    path = path + [start]
    print(path)
    if (start == end):
        return [path]
    if not start in graph:
        return None
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_path(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
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
def bfs_tree(g,start,tree,nid,next_n):
    """
    广度优先遍历有向图
    :param graph: DirectWeightGraph
    :param start: LoginPage
    :return: bfs_tree
    """
    pass

def traverse_po(g,start):
    """
    广度优先遍历有向图
    :param graph: DirectWeightGraph
    :param start: LoginPage
    :return: path
    """
    visited,queue = [],[start]
    while queue:
        node = queue.pop(0)
        for key,value in g[node].items():
            if key not in visited:
                visited.append(key)
                queue.append(value)
    return visited
def encoding_tree_node_id(temps):
    """
    快速命名节点id,思想：根据嵌套list,构建对应的节点id。
    保证节点命名不重复，建立一个字典来统计各个节点的出现次数
    同一棵树下不同路径子树相同，建立临时path，从当前list的第一个元素与之前的list相同位置元素进行比较，若第一个元素相同，
    则将对应list抽出放到path，当前list节点命名与path中的同位置相同元素一样；若不同，则将id命名为该元素与其当前计数的拼接
    str.
    :param temps:
    :return:
    """
    #first template的值直接作为其id
    temps_id = [temps[0]]
    #构建一个id计数器以对其节点id进行命名
    id_count_dict = dict(zip(temps_id[0],[1]*len(temps_id[0])))
    #Template总数
    len_temps = len(temps)
    #encoding id begin
    for i in range(1,len_temps):
        temp_path = []#将符合条件的temp存入临时path
        temp_path_loc = []#记录临时path在原始temps中的位置
        len_current_list = len(temps[i])
        for xi in temps[i]:
            if xi in id_count_dict.keys():
                id_count_dict[xi] = id_count_dict[xi] + 1
            else:
                id_count_dict[xi] = 1
        for k in range(len_current_list):
            if k == 0:
                for j in range(i):
                    if temps[i][k] == temps[j][k]:
                        temp_path.append(temps[j])
                        temp_path_loc.append(j)
                        if len(temps_id) < i+1:
                            temps_id.append([temps_id[j][k]])
                        else:
                            pass
                    else:
                        pass
                if len(temp_path) == 0:
                    temp_path.append(temps[i])
                    temp_path_loc.append(j)
                    temps_id.append([])
                    for xk in range(len_current_list):
                        if temps[i][xk] in id_count_dict.keys():
                            temps_id[i].append(temps[i][xk]+str(id_count_dict[temps[i][xk]]))
                        else:
                            temps_id[i].append(temps[i][xk])
                    break
            else:
                temp_path01 = []
                temp_path_loc01 = []
                for x in range(len(temp_path)):
                    if (k+1) <= len(temp_path[x]):
                        if temps[i][k] == temp_path[x][k]:
                            temp_path01.append(temp_path[x])
                            temp_path_loc01.append(temp_path_loc[x])
                            if len(temps_id[i]) < k+1:
                                temps_id[i].append(temps_id[temp_path_loc[x]][k])
                            else:
                                pass
                        else:
                            pass
                    else:
                        continue
                temp_path = temp_path01
                temp_path_loc = temp_path_loc01
        if len(temps_id[i]) < len(temps[i]):
            for y in range(len(temps_id[i]),len(temps[i])):
                if temps[i][y] in id_count_dict.keys():
                    temps_id[i].append(temps[i][y]+str(id_count_dict[temps[i][y]]))
                else:
                    temps_id[i].append(temps[i][y])
    return temps_id
if __name__ == '__main__':
    # dic=parse_pagefile.get_graph()
    # print(dic)
    g={"LoginPage": {"login": "HomePage"},
       "HomePage": {"goto_user": "UserPage", "goto_stat": "StatPage", "goto_region": "RegionPage",
                    "goto_sys": "SysPage", "goto_promotion": "PromotionPage", "goto_good": "GoodPage",
                    "logout": "HomePage"},
       "ModifyPasswordPage": {"modify_password": "ModifyPasswordPage"},
       "UserPage": {"search_user": "UserPage", "add_user": "UserPage", "get_user_data": "UserPage"},
       "AddressPage": {"search_address": "AddressPage"},
       "CollectPage": {"search_collect": "CollectPage"},
       "FootprintPage": {"search_footprint": "FootprintPage"},
       "HistoryPage": {"search_history": "HistoryPage"},
       "FeedbackPage": {"search_feedback": "FeedbackPage"},
       "RegionPage": {"search_region": "RegionPage"},
       "BrandPage": {"add_brand": "BrandPage", "search_brand": "BrandPage"},
       "CategoryPage": {"search_category": "CategoryPage"},
       "OrderPage": {"search_order": "OrderPage"},
       "IssuePage": {"search_issue": "IssuePage"},
       "KeywordPage": {"search_keyword": "KeywordPage", "add_keyword": "KeywordPage"},
       "GoodPage": {"search_good": "GoodPage", "add_good": "GoodPage"},
       "CreatePage": {"add_good": "GoodPage"},
       "CommentPage": {"search_comment": "CommentPage"},
       "PromotionPage": {"search_promotion": "PromotionPage", "add_ad": "AdPage"},
       "AdPage":{"add_ad":"AdPage"},
       "TopicPage": {"add_topic": "TopicPage"},
       "Groupon_rulePage": {"add_rule": "Groupon_rulePage", "search_rule": "Groupon_rulePage"},
       "Groupon_activityPage": {"search_activity": "Groupon_activityPage"},
       "SysPage": {"add_admin": "SysPage"},
       "OsPage": {"add_object": "OsPage"},
       "StatPage":{"search_stat":"StatPage"}}
    #print(g.edges)
    # print(traverse_po(g,'LoginPage'))
    # bfs_po = traverse_po(g,'LoginPage')
    tree = bfs_tree(g,'LoginPage')
    tree.show()
    #print(g.adjmt)
    #

