# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 19:54
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
去除文本文件中的空行
stopwords.txt去空行前的文件，new.txt去空行后的文件
"""
import sys
import os
def delete(filepath):
    f=open(filepath)
    path = 'D:\code\python\PageOs\POparse\cluster'
    f_new = open(os.path.join(path,'new_index.html'), 'w')
    for line in f.readlines():
        data = line.strip()
        if len(data) != 0:
            print(data)
            f_new.write(data)
            f_new.write('\n')
    f.close()
    f_new.close()

if __name__ == '__main__':

    # delete( 'D:\code\python\PageOs\POparse\cluster\stopwords.txt')
    delete('D:\code\python\PageOs\POparse\doms\index.html')