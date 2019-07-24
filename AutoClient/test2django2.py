#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
# Author :Yangky
# @TIME : 2019-07-16 16:59

import requests

data = {
    'status': True,
    "server_info": {
        'cpu': 'xxx',
        'mem': 'xxx',
        'disk': 'xxx',
        'nic': 'xxx',
    }
}

response = requests.post(url='http://127.0.0.1:8000/api/asset/', json=data,
                         headers={'authkey': 'f3e29cf01fae761fbb820c0e54df5cd8|1563268514.64336'})

print(response.text)