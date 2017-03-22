#!/usr/bin/env python
#-*-coding:utf-8-*-

import socket

HOST='127.0.0.1'
PORT=9001
BUFSIZE=1024
ADDR=(HOST,PORT)
tcpSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSock.connect(ADDR)

while True:
    recvdata=tcpSock.recv(BUFSIZE)
    print "Return data: %s" % recvdata
    senddata=raw_input("Send message>>")
    tcpSock.send(senddata)
