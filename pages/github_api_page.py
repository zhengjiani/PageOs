# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 20:51
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""查询用户，获取该用户所有的repos"""
import json
class GetRepoPage():
    @staticmethod
    def get_repos_list():
        import requests
        response = requests.get("https://api.github.com/users/zhengjiani/repos")
        r_dict=response.json()
        repos = []
        for i in range(len(r_dict)):
            repos.append(r_dict[i]['full_name'])
        return repos
if __name__ == "__main__":
    print(GetRepoPage.get_repos_list())