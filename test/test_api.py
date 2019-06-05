# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 14:36
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
import requests
from requests_oauthlib import OAuth1
from requests.auth import HTTPBasicAuth
from requests_oauth2 import OAuth2BearerToken
# r=requests.get('https://api.github.com/user',auth=HTTPBasicAuth('zhengjiani','zhengjiani88'))
# print(r.headers)
import requests
url = "https://api.github.com"
headers = {
    'Authorization': "Bearer bdee667870ce62606b040ff6a573650b68109dbd",
    }
response = requests.get(url, headers=headers)
print(response.text)