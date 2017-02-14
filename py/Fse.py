#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import socket
import sys
import pymysql.cursors

from thrift.TMultiplexedProcessor import TMultiplexedProcessor
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TTransport, TSocket

sys.path.append('./../gen-py')
from first import upAddress
from first import upName
from first import upPwd
# TMultiplexProtocol


class db:
        # 初始化数据库连接

    def __init__(self):
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '',
            'db': 'test',
            'charset': 'utf8',
            'cursorclass': pymysql.cursors.DictCursor,
        }

        # Connect to the database
        self.connection = pymysql.connect(**config)
        self.cursor = self.connection.cursor()

    def add(self, name, age, sex):
        try:
            sql = 'insert into test(name,age,sex) values(%s,%s,%s)'
            self.cursor.execute(sql, (name, age, sex))
            self.connection.commit()
        finally:
            self.connection.close()

    def select(self, id):
        try:
            sql = 'select * from test where id=%s'
            self.cursor.execute(sql, id)
            result = self.cursor.fetchone()
            # self.connection.commit()
            return result
        finally:
            self.connection.close()


class upAddressHandler:

    def EditAddress(self, id, address):

        return address


class upNameHandler:

    def EditName(self, id, name):
        D = db()
        #D.add('zl', 23, 1)
        sql = 'UPDATE test set name = %s where id = %s'
        D.cursor.execute(sql, (name, id))
        D.connection.commit()
        D.connection.close()
        # 严格的返回类型控制,直接返回int 的id会挂,要与thrift定义时的返回类型一致
        return str(id)
        # return 'ssss11111'


class upPwdHandler:

    def EditPassword(self, id, password):
        return password
# print(123)
#transport = TSocket.TServerSocket(host='localhost', port=9090)
transport = TSocket.TServerSocket("localhost", 9092)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

upAddressprocessor = upAddress.Processor(upAddressHandler())
upNameprocessor = upName.Processor(upNameHandler())
upPwdprocessor = upPwd.Processor(upPwdHandler())


processor = TMultiplexedProcessor()  # 使用TMultiplexedProcessor接收多个处理

processor.registerProcessor("upname", upNameprocessor)  # 注册upname服务
processor.registerProcessor("upaddress", upAddressprocessor)  # 注册upaddress服务
processor.registerProcessor("uppwd", upPwdprocessor)  # 注册upaddress服务


server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

# 开始监听请求
server.serve()

# print("Starting thrift server in python...")

# print("done!")
