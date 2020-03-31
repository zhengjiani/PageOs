# -*- encoding: utf-8 -*-
"""
@File    : generate_tree.py
@Time    : 2020/3/2 9:57 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from treelib import Node,Tree
from random import choice,random
from collections import deque, Counter


class Trans_tree(object):
    def __init__(self,pog_dic):
        self.tree = Tree()
        self.pog_dic = pog_dic

    def bfs_create_tree(self,root):
        po_queue = deque()
        po_queue.append(root)
        visited = []
        tree_dic = {}
        po_hash = {}
        po_hash[0] = root
        i = 0
        while len(po_queue) > 0:
            node = po_queue.popleft()
            if node not in visited:
                visited.append(node)
                tree_dic[node] = list(self.pog_dic[node].values())
                for index,child in enumerate(list(self.pog_dic[node].values())):
                    i = i + 1
                    self.tree.create_node(child, i, parent= i-(index+1))
                    po_hash[i] = child
                    po_queue.append(child)


        return tree_dic,po_hash

    def tran_tree(self):
        nodes = set(self.pog_dic.keys())
        root = choice(list(nodes))
        self.tree.create_node(root, 0)
        tree_dic,po_hash = self.bfs_create_tree(root)
        return tree_dic,self.tree,po_hash



# if __name__ == "__main__":
#     tree = Tree()
#     pog_dic = {
#         "AddNewPetPage": {
#             "add_new_pet": "DetailPage"
#         },
#         "AddNewVisitPage": {
#             "add_visit": "DetailPage"
#         },
#         "DetailPage": {
#             "goto_add_pet": "AddNewPetPage",
#             "goto_edit": "EditOwnerPage",
#             "goto_edit_pet": "PetPage",
#             "goto_pet": "PetPage",
#             "goto_visit": "AddNewVisitPage"
#         },
#         "EditOwnerPage": {
#             "edit_info": "DetailPage"
#         },
#         "FindPage": {
#             "goto_detail_page": "DetailPage"
#         },
#         "HomePage": {
#             "goto_Veter": "VeterPage",
#             "goto_register": "RegisterPage",
#             "goto_search": "FindPage"
#         },
#         "PetPage": {
#             "edit_pet": "DetailPage"
#         },
#         "RegisterPage": {
#             "regist_owner": "FindPage"
#         },
#         "VeterPage": {}
#     }
#     # 随机选择根节点
#     nodes = set(pog_dic.keys())
#     root = choice(list(nodes))
#     # print("根节点",root)
#     tree.create_node(root, 0)
#     # bfs_search(root)
#     # tree.show()
#     tree_dic = bfs_create_tree(root)
#     print(tree_dic)
#     # create_tree(root,tree_dic)
#     tree.show()
#     print(tree.paths_to_leaves())
#     print(tree.leaves())
