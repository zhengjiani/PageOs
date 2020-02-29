from bs4 import BeautifulSoup
import os
import pandas as pd

base_dir = os.path.dirname(__file__)
def deal(dic, soup):
    '''
    递归获取孩子节点
    :param dic: 字典
    :param soup: bs4
    :return:
    '''
    for child in soup.children:
        if child.name:
            dic[child.name] = {}
            deal(dic[child.name], child)


def tree(dic):
    '''
    字典转化为RTED命令行中树的表示形式
    :param dic:
    :return:
    '''
    return str(dic).replace(':', '').replace('{}', '}').replace(',', '{').replace(' ', '')


def cal(tree_1, tree_2):
    '''
    :param tree_1: DOM树1
    :param tree_2: DOM树2
    :return: 相似度0-1
    '''
    os.chdir("/Users/zhengjiani/PycharmProjects/PageOs_v0.1")
    s = "java -jar RTED_v1.2.jar -t {0} {1} -o -v".format(tree_1, tree_2)
    r = os.popen(s)
    str1 = r.readlines()[0]
    return str1.split(' ')[-1]


if __name__ == '__main__':
    path = os.path.join(base_dir, 'doms')
    files = os.listdir(path)
    dic_DOMRTED = {}
    print("-------------DOMRTED计算开始---------------")
    dic1 = {}
    dic2 = {}
    for file1 in files:
        html_doc1 = open(os.path.join(path, file1), encoding="unicode_escape").read()
        soup1 = BeautifulSoup(html_doc1, 'html.parser')
        deal(dic1, soup1)
        tree1 = tree(dic1)
        dic_DOMRTED[file1] = {}
        for file2 in files:
            html_doc2 = open(os.path.join(path, file2), encoding="unicode_escape").read()
            soup2 = BeautifulSoup(html_doc2, 'html.parser')
            deal(dic2, soup2)
            tree2 = tree(dic2)
            dic_DOMRTED[file1][file2] = cal(tree1, tree2)
    print(dic_DOMRTED)
        # d = pd.DataFrame.from_dict(dic_DOMRTED)
        # print(d)
        # d.to_csv("dom_rted.csv")
    print("-------------DOMRTED计算结束---------------")
