# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 15:26
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from anytree import Node, RenderTree
udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)
for pre, fill, node in RenderTree(udo):
    print("%s%s" % (pre, node.name))
from anytree.exporter import DotExporter
DotExporter(udo).to_picture("udo.png")