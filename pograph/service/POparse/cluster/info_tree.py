from bs4 import BeautifulSoup
import os
import pandas as pd
def deal(dic, soup):
    for child in soup.children:
        if child.name:
            dic[child.name] = {}
            deal(dic[child.name], child)
def tree(dict):
    return str(dict).replace(':','').replace('{}','}').replace(',','{').replace(' ','')
def cal(tree1,tree2):
    os.chdir("D:\\code\\python\\PageOs")
    s = "java -jar RTED_v1.2.jar -t {0} {1} -o -v".format(tree1, tree2)
    r=os.popen(s)
    str1 = r.readlines()[0]
    return str1.split(' ')[-1]

if __name__ == '__main__':
    path = 'D:\code\python\PageOs\POparse\doms'
    files = os.listdir(path)
    dic_DOMRTED={}
    print("-------------DOMRTED计算开始---------------")
    dic1 = {}
    dic2 = {}
    for file1 in files:
        html_doc1 = open(os.path.join(path, file1), encoding='UTF-8').read()
        soup1 = BeautifulSoup(html_doc1, 'html.parser')
        deal(dic1, soup1)
        tree1 = tree(dic1)
        dic_DOMRTED[file1]={}
        for file2 in files:
            html_doc2 = open(os.path.join(path, file2), encoding='UTF-8').read()
            soup2 = BeautifulSoup(html_doc2, 'html.parser')
            deal(dic2, soup2)
            tree2 = tree(dic2)
            dic_DOMRTED[file1][file2] = cal(tree1,tree2)
        d = pd.DataFrame.from_dict(dic_DOMRTED)
        print(d)
        d.to_csv("dom_rted.csv")
    print("-------------DOMRTED计算结束---------------")




