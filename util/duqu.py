# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 10:10
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
#使用钩子函数过滤.yml文件
def pytest_collect_file(parent,path):
    # 获取文件.yml文件
    if path.ext == ".yml" and path.basename.startswith("test"):
        return YamlFile(path,parent)