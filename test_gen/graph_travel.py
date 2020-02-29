# -*- encoding: utf-8 -*-
"""
@File    : graph_travel.py
@Time    : 2020/1/12 10:39 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from collections import defaultdict
class DGraph(object):
    """Directed graph"""
    def __init__(self):
        self.edges = defaultdict(set)

    def add_edges(self, *pairs):
        """Add edges to the graph
            there's an edge in the graph from u to v
        """
        for u, v in pairs:
            self.edges[u].add(v)
            if v not in self.edges:
                self.edges[v] = set()

    def successors(self, v):
        """
        Iterator over all the successors of node v in the graph
        :param v:
        :return:
        """
        return iter(self.edges[v])

    def nodes(self):
        """Iterator over all the nodes in the graph."""
        return iter(self.edges)

    def render(self,filename='graph.png'):
        """
        Render the graph to a PNG file using pygraphviz
        :param filename:
        :return:
        """
        try:
            from graphviz import Digraph
            dot = Digraph(comment=filename)
            for u in self.edges:
                for v in self.edges[u]:
                    dot.edge(u,v)

            dot.render('graph.png', view=True)
        except ImportError as e:
            print(e)

# 基础的深度遍历算法
def dfs(graph,root,visitor):
    """
    DFS over a graph
    :param graph:
    :param root:
    :param visitor:
    :return:
    """
    visited = set()
    def dfs_walk(node):
        visited.add(node)
        visitor(node)
        for succ in graph.successors(node):
            if not succ in visited:
                dfs_walk(succ)
    dfs_walk(root)

# 拓扑排序
def postorder(graph,root):
    """Return a post-order ordering"""
    visited = set()
    order = []
    def dfs_walk(node):
        visited.add(node)
        for succ in graph.successors(node):
            if not succ in visited:
                dfs_walk(succ)
        order.append(node)
    dfs_walk(root)
    return order

# 无根节点的图
def postorder_unrooted(graph):
    """
    unrooted post-order traversal of a graph
    :param graph:
    :return:
    """
    allnodes = set(graph.nodes())
    visited = set()
    orders = []
    def dfs_walk(node):
        visited.add(node)
        for succ in graph.successors(node):
            if not succ in visited:
                dfs_walk(succ)
        orders[-1].append(node)
    while len(allnodes) > len(visited):
        # while there are still unvisited nodes in the graph,pick one at random
        # and restart the traversal from it
        remaining = allnodes - visited
        root = remaining.pop()
        orders.append([])
        dfs_walk(root)
    return orders

def postorder_3color(graph, root):
    """Return a post-order ordering of nodes in the graph
    prints CYCLE notifications when graph cycles ("back edges") are discovered
    """
    color = dict()
    order = []
    def dfs_walk(node):
        color[node] = 'grey'
        for succ in graph.successors(node):
            if color.get(succ) == 'grey':
                print('CYCLE:{0}-->{1}'.format(node, succ))
            if succ not in color:
                dfs_walk(succ)
        order.append(node)
        color[node] = 'black'
        dfs_walk(root)
        return order

if __name__ == '__main__':
    gg = DGraph()
    # gg.add_edges(('x', 't'), ('x', 'b'), ('x', 'c'))
    # gg.add_edges(('c', 'e'), ('e', 'm'), ('m', 'c'))
    # gg.add_edges(('b', 'd'), ('e', 'd'), ('t', 'b'))
    # gg.add_edges(('d', 'g'), ('g', 'd'))
    gg.add_edges(('OwnerInfo', 'Find'), ('OwnerInfo', 'AddPet'),
                 ('OwnerInfo', 'EditOwner'), ('OwnerInfo', 'Index'),
                 ('OwnerInfo', 'New Visit'))
    gg.add_edges(('AddPet', 'OwnerInfo'), ('AddPet', 'Find'),
                 ('AddPet', 'Index'))
    gg.add_edges(('EditOwner', 'Find'), ('EditOwner', 'Index'))
    gg.add_edges(('New Visit', 'Index'), ('New Visit', 'Find'))
    gg.add_edges(('Index', 'Find'))
    gg.add_edges(('Find', 'Owners'), ('Find', 'Index'), ('Find', 'AddOwner'))
    gg.add_edges(('AddOwner', 'Find'), ('AddOwner', 'Index'), ('AddOwner', 'Owners'))
    gg.add_edges(('Owners', 'Find'), ('Owners', 'Owners'), ('Owners', 'Index'), ('Owners', 'OwnerInfo'))
    gg.render()

    print('all nodes')
    print(list(gg.nodes()))

    print('post', postorder(gg, 'OwnerInfo'))
    print('post_unrooted', postorder_unrooted(gg))
    print('post_3color', postorder_3color(gg, 'OwnerInfo'))
