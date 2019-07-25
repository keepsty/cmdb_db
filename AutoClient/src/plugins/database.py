#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
# Author :Yangky
# @TIME : 2019-07-25 16:54

import os
import traceback
from .base import BasePlugin
from lib.response import BaseResponse
from config import settings
import pymysql


class GetServerDBInfo(object):
    '''
    获取server的cmdb数据库 table中数据库list
    '''

    def __init__(self, user, host, port, passwd, db):
        self.user = user
        self.host = host
        self.port = port
        self.passwd = passwd
        self.db = db
        self.dbinfo = None

    def getinfo(self, sql, *args):
        conn = pymysql.connect(host=self.host, user=self.user, port=self.port, password=self.passwd, database=self.db,
                               charset='utf8')
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql, args)
        if sql.find('select') >= 0 or sql.find('show') >= 0:
            self.dbinfo = cur.fetchall()
        else:
            conn.commit()
        cur.close()
        conn.close()
        if self.dbinfo:
            return self.dbinfo


class DatabasePlugin(BasePlugin):
    def linux(self):
        response = BaseResponse()
        try:
            if self.test_mode:
                from config.settings import BASEDIR

                output = open(os.path.join(BASEDIR, 'files/database.out'), 'r').read()
            else:
                database_obj = GetServerDBInfo(user=settings.SERVER_DATABASE_CONF['user'],
                                               host=settings.SERVER_DATABASE_CONF['host'],
                                               port=settings.SERVER_DATABASE_CONF['port'],
                                               passwd=settings.SERVER_DATABASE_CONF['password'],
                                               db=settings.SERVER_DATABASE_CONF['db'])

                ser_db_list = database_obj.getinfo(settings.SERVER_DATABASE_CONF['sql'], )

                for item in ser_db_list:
                    for subject in settings.CLIENT_DATABASE_CONF['sql_list']:
                        client_obj = GetServerDBInfo(user=settings.CLIENT_DATABASE_CONF['user'],
                                                     host=item['ip'],
                                                     port=item['port'],
                                                     passwd=settings.CLIENT_DATABASE_CONF['password'])
                        cli_db_info = client_obj.getinfo(settings.CLIENT_DATABASE_CONF['sql_list'][subject])
                        response.data[subject] = cli_db_info
        except Exception as e:
            msg = "%s Mysql info collect fail %s"
            self.logger.log(msg % (self.hostname, traceback.format_exc()), False)
            response.status = False
            response.error = msg % (self.hostname, traceback.format_exc())
        return response


if __name__ == '__main__':
    obj1 = DatabasePlugin
    obj1.linux()
