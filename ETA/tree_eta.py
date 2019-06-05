# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 19:28
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from anytree import Node,RenderTree
from anytree.exporter import DotExporter
from collections import Counter


def find_all_path(graph,paths=[]):
    lis = list(graph.keys())
    visited = []
    for k, v in dic.items():
        visited.append(k)
        for k_val, v_val in v.items():
            # UserListPage 叶子节点
            if v_val not in lis:
                path=find_shortest_path(graph, lis[0], v_val)
                paths.append(path)
            # UserPage 叶子节点
            elif v_val == k:
                path=find_shortest_path(graph, lis[0], v_val) + [v_val]
                paths.append(path)
            # LoginPage 叶子节点，去环情况
            elif v_val in visited:
                path=[lis[0], k, v_val]
                paths.append(path)
    return paths
# print(nodes)
def bfs(graph,start):
    visited,queue = set(),[start]
    while queue:
        node = queue.pop(0)
        visited.add(node)
        # 处理叶子节点情况，即node not in dic.keys()
        # 处理UserListPage , 即不再加入队列中
        if node not in list(graph.keys()):
            # leaf = Node(node,parent=nod)
            break
        else:
            for k_val, v_val in graph[node].items():
                if v_val not in visited:
                    queue.append(v_val)
                # v_val曾经被访问过，如 HomePage -> LoginPage
                else:
                    visited.add(v_val)
                    break
                    # leaf = Node(v_val,parent=node)
    return visited
# for pre, fill, node in RenderTree(root):
#     print("%s%s" % (pre, node.name))
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for k_val,node in graph[start].items():
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest
if __name__ == "__main__":
    dic = {'LoginPage': {'login': 'HomePage'},
           'HomePage': {'goto_user': 'UserPage', 'logout': 'LoginPage'},
           'UserPage': {'add_user': 'UserListPage', 'remove_user': 'UserListPage', 'search_user': 'UserPage'}
           }
    # print(find_all_path(dic))
    paths = find_all_path(dic)
    print(paths)


