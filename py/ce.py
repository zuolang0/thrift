#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
sys.path.append('./../gen-py')
import json
from hello import HelloWorld
# from topology import Nimbus
# from topology import ttypes

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

# try:
#     transport = TSocket.TSocket('192.168.70.168', 6627)
#     transport = TTransport.TBufferedTransport(transport)
#     protocol = TBinaryProtocol.TBinaryProtocol(transport)
#     client = Nimbus.Client(protocol)
#     spout = {'spouts': 'RandomSentenceSpout'}
#     bolt = {'bolts': 'SplitSentenceBolt'}
#     topologys = ttypes.StormTopology(
#         spout, bolt)
#     transport.open()

#     print("client - sayHello")
#     name = 'testcount'
#     uploadedJarLocation = '/usr/local/storm4/local/nimbus/inbox/stormjar-6499eee5-9c25-444c-92f1-6beb2d644395.jar'
#     data = {

#     }
#     # 'spouts': '',
#     # 'bolts': '',
#     jsonConf = json.dumps(data)
#     print("server - " + client.submitTopology(name,
# uploadedJarLocation, jsonConf, topologys))

#     # print("client - say")
#     # msg = client.say("Hello!")
#     # print("server - " + msg)

#     transport.close()

# except Thrift.TException as ex:
#     print("%s" % (ex.message))
try:
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = HelloWorld.Client(protocol)
    transport.open()

    #print("client - sayHello")
    print("server - " + client.sayHello())

    # print("client - say")
    # msg = client.say("Hello!")
    # print("server - " + msg)

    transport.close()

except Thrift.TException as ex:
    print("%s" % (ex.message))
