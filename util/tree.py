# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 20:13
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from treelib import Node,Tree
node = Node()
tree = Tree()
tree.create_node("Harry","harry")#root node
tree.create_node("Jane","jane",parent="harry")
tree.create_node("Bill","bill",parent="harry")
tree.create_node("Diane", "diane", parent="jane")
tree.create_node("Mary", "mary", parent="diane")
tree.create_node("Mark", "mark", parent="jane")
tree.show()
#打印节点标签
print(','.join([tree[node].tag for node in tree.expand_tree(mode=Tree.DEPTH)]))
#过滤节点标签
print(','.join([tree[node].tag for node in tree.expand_tree(filter = lambda x:x.identifier != 'diane')]))
#获得某一节点的子树
sub_t = tree.subtree('diane')
sub_t.show()
#在原来的树上粘一棵新树
new_tree = Tree()
new_tree.create_node("n1",1)#root node
new_tree.create_node("n2",2,parent=1)
new_tree.create_node("n3",3,parent=1)
tree.paste('bill',new_tree)
tree.show()
#移去已经存在的节点,如果移去的是根节点，则子树也移了
tree.remove_node(1)
tree.show()
#移动节点改变父节点
tree.move_node('mary','harry')
tree.show()
#树的深度
print(tree.depth())
#获取节点标签
node = tree.get_node("bill")
tree.depth(node)


#保存树
#tree.save2file('tree.txt')