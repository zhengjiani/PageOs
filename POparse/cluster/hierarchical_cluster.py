# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 20:00
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
层次聚类的简单例子
"""
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import numpy as np

X = np.array([[1, 2], [1, 4], [1, 0],
              [4,2],[4,4],[4,0]])
clustering=AgglomerativeClustering().fit(X)

clustering.labels_array([1,1,1,0,0,0])
