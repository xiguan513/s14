#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import SocketServer
from  time import ctime

class MyTCPHandler(SocketServer.BaseRequestHandler):
    #继承BaseRequestHandler基类，然后必须重新handle方法，并在handle方法里面实现与客户端的所有交互

    def handle(self):
        while True:
            data=self.request.recv(1024)#设置接收1024字节数据
            if not data:
                break
            else:
                print '[%s] %s' % (ctime(),data)
            self.request.sendall('[%s] %s' % (ctime(),data))

if __name__=="__main__":
    HOST,PORT='127.0.0.1',8002
    ADDR=(HOST,PORT)
    server=SocketServer.ThreadingTCPServer(ADDR,MyTCPHandler)
    server.serve_forever()
