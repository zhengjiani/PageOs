# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 16:00
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
import pytest

#设置测试钩子
@pytest.fixture()
def test_url():
    return "http://www.baidu.com"