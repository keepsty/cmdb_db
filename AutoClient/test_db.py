# from concurrent.futures import ThreadPoolExecutor
# from concurrent.futures import ProcessPoolExecutor
# import time
# def task(arg):
#     print(arg)
#     time.sleep(1)
#
# # pool = ProcessPoolExecutor(5)
# pool = ThreadPoolExecutor(5)
#
# for i in range(50):
#     pool.submit(task,i)


import pymysql
import re
from config import settings


class GetServerDBInfo(object):
    '''
    获取server的cmdb数据库 table中数据库list
    '''

    def __init__(self, user, host, port, passwd):
        self.user = user
        self.host = host
        self.port = port
        self.passwd = passwd

    def getinfo(self, sql, *args):
        dbinfo = None
        conn = pymysql.connect(host=self.host, user=self.user, port=self.port, password=self.passwd,
                               charset='utf8')
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql, args)
        if sql.find('select') >= 0 or sql.find('show') >= 0:
            dbinfo = cur.fetchall()
        else:
            conn.commit()
        cur.close()
        conn.close()
        if dbinfo:
            return dbinfo

    # class DatabasePlugin(object):
    #     response = {}
    #
    #     def linux(self):
    #
    #         try:
    #
    #             database_obj = GetServerDBInfo(user=settings.SERVER_DATABASE_CONF['user'],
    #                                            host=settings.SERVER_DATABASE_CONF['host'],
    #                                            port=settings.SERVER_DATABASE_CONF['port'],
    #                                            passwd=settings.SERVER_DATABASE_CONF['password'],
    #                                            db=settings.SERVER_DATABASE_CONF['db'])
    #
    #             ser_db_list = database_obj.getinfo(settings.SERVER_DATABASE_CONF['sql'], )
    #
    #             for item in ser_db_list:
    #                 print(item)
    #
    #             # shell_command = "/usr/local/mysql/bin/mysql -u'{}' -p'{}' -h'{}' -P{} -e '{}'".format(
    #             #     settings.DATABASE_CONF['user'], settings.DATABASE_CONF['password'], settings.DATABASE_CONF['host'],
    #             #     settings.DATABASE_CONF['port'], '')
    #
    #             # output = self.exec_shell_cmd(shell_command)
    #
    #         # response.data = self.parse(item)
    #         except Exception as e:
    #             print(e)
    #
    #         return ser_db_list


def linux():
    response = {'dblist': []}
    try:

        database_obj = GetServerDBInfo(user=settings.SERVER_DATABASE_CONF['user'],
                                       host=settings.SERVER_DATABASE_CONF['host'],
                                       port=int(settings.SERVER_DATABASE_CONF['port']),
                                       passwd=settings.SERVER_DATABASE_CONF['password'])

        ser_db_list = database_obj.getinfo(settings.SERVER_DATABASE_CONF['sql'], )
        # print(ser_db_list)

        for item in ser_db_list:
            for subject in settings.CLIENT_DATABASE_CONF['sql_list']:
                client_obj = GetServerDBInfo(user=settings.CLIENT_DATABASE_CONF['user'],
                                             host=item['ip'],
                                             port=item['port'],
                                             passwd=settings.CLIENT_DATABASE_CONF['password'])
                cli_db_info = client_obj.getinfo(settings.CLIENT_DATABASE_CONF['sql_list'][subject])
                response[subject] = cli_db_info

    # shell_command = "/usr/local/mysql/bin/mysql -u'{}' -p'{}' -h'{}' -P{} -e '{}'".format(
    #     settings.DATABASE_CONF['user'], settings.DATABASE_CONF['password'], settings.DATABASE_CONF['host'],
    #     settings.DATABASE_CONF['port'], '')

    # output = self.exec_shell_cmd(shell_command)

    # response.data = self.parse(item)
    except Exception as e:
        print(e)

    return response


obj_1 = linux()
for subject in settings.CLIENT_DATABASE_CONF['sql_list']:
    for i in obj_1[subject]:
        print(i)
