#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
# Author :Yangky
# @TIME : 2019-07-16 11:24


import requests
import hashlib
import time

cli_key = 'efmgkamgkqo23eo3r9madmorq3ipo'
cur_time = time.time()

key_time = "{}{}" .format(cli_key, cur_time)

m = hashlib.md5()
m.update(bytes(key_time, encoding='utf-8'))
auth_key = m.hexdigest()

auth_key_time = '{}|{}'.format(auth_key,cur_time)
print(auth_key_time)

data = {
    'status': True,
    "server_info": {
        'cpu': 'xxx',
        'mem': 'xxx',
        'disk': 'xxx',
        'nic': 'xxx',
    }
}
# requests.get(url='http://127.0.0.1:8000/api/asset/?k1=123',)
# requests.get(url='http://127.0.0.1:8000/api/asset/', params={'k1': 123})
response = requests.post(url='http://127.0.0.1:8000/api/asset/', json=data,
                         headers={'authkey': auth_key_time})  # json格式数据传到接口的body中去。
# get 方法能传输get数据
# post 方法能传输post和get数据
# django中，request.POST、request.GET 只能接受请求头、url的数据
# request.body 能存放请求体数据

print(response.text)
