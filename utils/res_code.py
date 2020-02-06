# -*- encoding: utf-8 -*-
"""
@File    : res_code.py
@Time    : 2020/1/4 4:52 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# response code and msg
class ResponseCode(object):
    SUCCESS = 0
    FAIL = -1
    NO_RESOURCE_FOUND = 40001 #未找到资源
    INVALID_PARAMETER = 40002 #参数无效
    ACCOUNT_OR_PASS_WORD_ERR = 40003 #账户或密码错误

class ResponseMessage(object):
    SUCCESS = "成功"
    FAIL = "失败"
    NO_RESOURCE_FOUND = "未找到资源"
    INVALID_PARAMETER = "参数无效"
    ACCOUNT_OR_PASS_WORD_ERR = "账户或密码错误"