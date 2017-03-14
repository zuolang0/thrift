#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import sys
sys.path.append('./../gen-py')
from hello import HelloWorld
# from hello.ttpyes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class HelloWorldHandler:

    def sayHello(self):
        return "helloworldssss"

handler = HelloWorldHandler()
processor = HelloWorld.Processor(handler)
transport = TSocket.TServerSocket("127.0.0.1", 9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting thrift server in python...")
server.serve()
print("done!")
