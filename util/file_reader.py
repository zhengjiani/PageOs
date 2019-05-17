# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 13:28
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
import yaml
import os

class YamlReader:
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在')
        self._data = None


