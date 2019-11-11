# -*- encoding: utf-8 -*-
"""
@File    : hierarchical_stat.py
@Time    : 2019/11/9 9:44 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import matplotlib.pyplot as plt
import operator
# 层次聚类
from pograph.service.POparse.cluster.dom_distance import DOMString
from collections import defaultdict
dom_dic = DOMString()
dic = dom_dic.get_domdict()
pair_dic = {}
for k,v in dic.items():
    for k1,v1 in v.items():
        pair_dic[(k,k1)] = float(v1)
# 聚类前
print(pair_dic)
print(len(dic.keys()))
# 聚类后
new_dic = {}
clust_dic = defaultdict(defaultdict)
for k1,v1 in pair_dic.items():
    lis = []
    for k2,v2 in pair_dic.items():
        if v1<1 and operator.eq(v1,v2) and k1[0] == k2[0]:
            lis.append(k2[1])
    new_dic[k1[0]+' sim='+str(v1)] = lis
    clust_dic[k1[0]][v1]=len(lis)
print(new_dic)
print(clust_dic)
nodes = list(clust_dic.keys())
fig = plt.figure(figsize=(20,20))
fig.subplots_adjust(top=0.8,hspace=0.4,wspace=0.4)

for j in range(1, len(nodes)):
    plt.subplot(9, 9, j)
    plt.title(nodes[j-1])
    # plt.xlabel("sim")
    # plt.ylabel("num")
    plt.scatter(clust_dic[nodes[j-1]].keys(), clust_dic[nodes[j-1]].values())
plt.savefig("/Users/zhengjiani/PycharmProjects/PageOs_latest/pograph/service/POparse/cluster/images/total.png")
plt.show()