# -*- encoding: utf-8 -*-
"""
@File    : getPath.py
@Time    : 2019/10/28 5:01 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import sys
class Path:
    def __init__(self):
        self.path = self.get_global_path('pograph')

    def get_global_path(self,dir_name):
        global_path = sys.path[0]
        for item in sys.path:
            if item.endswith(dir_name):
                global_path = item
                return global_path

    def get_current_path(self):
        return self.path

if __name__ == '__main__':
    print(Path().get_global_path(""))