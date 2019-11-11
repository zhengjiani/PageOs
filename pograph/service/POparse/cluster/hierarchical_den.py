# -*- encoding: utf-8 -*-
"""
@File    : hierarchical_den.py
@Time    : 2019/11/7 11:54 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# 层次聚类
import math
import numpy as np
from sklearn import datasets
from sklearn import cluster

def euler_distance(point1:np.ndarray,point2:list)-> float:
    """
    计算两点之间的欧拉距离，支持多维
    (后期可以改成两个页面之间的各种距离)
    :param point1:
    :param point2:
    :return:
    """
    distance = 0.0
    for a,b in zip(point1,point2):
        distance += math.pow(a-b,2)
    return math.sqrt(distance)
class ClusterNode(object):
    def __init__(self,vec,left=None,right=None,distance=-1,id=None,count=1):
        """
        :param vec: 保留两个数据聚类后形成新的中心
        :param left: 左节点
        :param right: 右节点
        :param distance: 两个节点的距离
        :param id: 用来标记哪些内容是计算过的
        :param count: 这个节点的叶子节点个数
        """
        self.vec = vec
        self.left = left
        self.right = right
        self.distance = distance
        self.id = id
        self.count = count
class Hiersrchical(object):
    def __init__(self,k=1):
        assert k>0
        self.k = k
        self.labels = None
    def fit(self,x):
        # 标记已经计算过的节点
        nodes = [ClusterNode(vec=v,id=i) for i,v in enumerate(x)]
        distances = {}
        point_num,future_num=np.shape(x) # 特征的维度
        self.labels = [ -1 ]*point_num
        currentclustid = -1
        while len(nodes) > self.k:
            min_dist = math.inf
            nodes_len = len(nodes)
            closet_part = None #表示最相似的两个聚类
            for i in range(nodes_len-1):
                for j in range(i+1,nodes_len):
                    # 为了不重复计算距离，保存在字典中
                    d_key = (nodes[i].id,nodes[j].id)
                    if d_key not in distances:
                        distances[d_key] = euler_distance(nodes[i].vec,nodes[j].vec)
                    d = distances[d_key]
                    if d<min_dist:
                        min_dist = d
                        closet_part = (i,j)
            # 合并两个聚类
            part1,part2 = closet_part
            node1,node2 = nodes[part1],nodes[part2]
            new_vec = [(node1.vec[i]*node1.count+node2.vec[i]*node2.count) / (node1.count+node2.count)
                       for i in range(future_num)]
            new_node = ClusterNode(vec=new_vec,
                                   left=node1,
                                   right=node2,
                                   distance=min_dist,
                                   id=currentclustid,
                                   count=node1.count+node2.count)
            currentclustid -= 1
            del nodes[part2],nodes[part1]
            nodes.append(new_node)
        self.nodes = nodes
        self.calc_label()

    def calc_label(self):
        """
        调取聚类的结果
        :return:
        """
        for i,node in enumerate(self.nodes):
            #将节点的所有叶子节点都分类
            self.leaf_traversal(node,i)
    def leaf_traversal(self,node:ClusterNode,label):
        """
        递归遍历叶子节点
        :param node:
        :param label:
        :return:
        """
        if node.left == None and node.right == None:
            self.labels[node.id] = label
        if node.left:
            self.leaf_traversal(node.left,label)
        if node.right:
            self.leaf_traversal(node.right,label)

iris = datasets.load_iris()
print(iris)
my = Hiersrchical(4)
my.fit(iris.data)
print(np.array(my.labels))

# 与官方聚类方法做对比
sk = cluster.AgglomerativeClustering(4)
sk.fit(iris.data)
print(sk.labels_)