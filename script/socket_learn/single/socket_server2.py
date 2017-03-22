#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket
from time import ctime

HOST="127.0.0.1"
PORT=9002
SIZE=1024
ADDR=(HOST,PORT)

tcpserSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpserSock.bind(ADDR)
tcpserSock.listen(5)

while True:
    tcpSer,addr=tcpserSock.accept()
    senddata="服务器端已经准备好了: %s" % ctime()
    tcpSer.sendall(senddata)
    recvdata=tcpSer.recv(SIZE)
    print recvdata
    while True:
        clidata=tcpSer.recv(SIZE)
        clisendata="%s %s" % (clidata.upper(),ctime())
        tcpSer.sendall(clisendata)
        print addr,">>",clidata


