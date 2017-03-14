#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from thrift.protocol.TMultiplexedProtocol import TMultiplexedProtocol
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol
# TBinaryProtocol：缺省简单的二进制序列化协议。
# TCompactProtocol：高效的二进制序列化协议。
sys.path.append('./../gen-py')

from first import upAddress
from first import upName
from first import upPwd


# TMultiplexProtocol

transport = TSocket.TSocket('localhost', 9084)
transport = TTransport.TBufferedTransport(transport)
protocol = TCompactProtocol.TCompactProtocol(transport)
#protocol = TBinaryProtocol.TBinaryProtocol(transport)


# 如果服务端使用TMultiplexedProcessor接收处理，客户端必须用TMultiplexedProtocol并且指定serviceName和服务端的一致
upname = TMultiplexedProtocol(protocol, "upName")
upaddress = TMultiplexedProtocol(protocol, "upAddress")
uppwd = TMultiplexedProtocol(protocol, "upPwd")
transport.open()
upname_client = upName.Client(upname)  # msg客户端
upaddress_client = upAddress.Client(upaddress)  # user客户端
uppwd_client = upPwd.Client(uppwd)  # user客户端

print(upname_client.EditName(1, 'nzl123'))
print(upaddress_client.EditAddress(12, 'address'))
print(uppwd_client.EditPassword(11, 'password'))

transport.close()


# try:
#     transport = TSocket.TSocket('localhost', 9090)
#     transport = TTransport.TBufferedTransport(transport)
#     protocol = TBinaryProtocol.TBinaryProtocol(transport)

#     transport.open()
#     upNameclient = upName.Client(protocol)

#     print("client - EditName")
#     print("server - " + upNameclient.EditName(2, 'name'))

#     client = upAddress.Client(protocol)
#     print("client - EditAddress")
#     print("server - " + client.EditAddress(2, 'address'))

#     # print("client - say")
#     # msg = client.say("Hello!")
#     # print("server - " + msg)

#     transport.close()

# except Thrift.TException as ex:
#     print("%s" % (ex.message))
