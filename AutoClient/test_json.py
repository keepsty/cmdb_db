#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
# Author :Yangky
# @TIME : 2019-07-15 22:58

from datetime import datetime
from datetime import date
import json


class JsonCustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, date):
            return o.strftime('%T-%m-%d')
        elif isinstance(o, Response):
            '''
            判断对象o是不是Response对象，如果是，那么就通过方法__dict__ 将类对象序化为字典
            '''
            return o.__dict__

        else:
            return json.JSONEncoder.default(self, o)


class Response(object):
    def __init__(self):
        self.status = True
        self.data = '12323232'


data = {
    'k1': 123,
    'k2': datetime.now(),
    'k3': Response()
}

ds = json.dumps(data, cls=JsonCustomEncoder)
print(ds)
