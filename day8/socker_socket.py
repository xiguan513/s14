#!/usr/bin/env python
#-*- coding:utf-8 -*-


import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data=self.request.recv(1024).strip()
                print "{} wrote:".format(self.client_address[0])
                print self.data
                self.request.sendall(self.data.upper())
            except Exception as e:
                print "断开连接",e
                break

if __name__=="__main__":
    HOST,PORT='192.168.1.75',9999
    sever=SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    sever.serve_forever()