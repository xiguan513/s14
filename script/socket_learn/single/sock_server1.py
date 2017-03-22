#!/usr/bin/env python
#-*-coding:utf-8-*-

import socket
import time

HOST='127.0.0.1'
PORT=9001
ADDR=(HOST,PORT)
BUFSIZE=1024


tcpSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSock.bind(ADDR)
tcpSock.listen(5)


while True:
    tcpSock_cli,addr = tcpSock.accept()
    while True:
        try:
            senddata="Ready to send a message [%s]" % time.ctime()
            tcpSock_cli.send(senddata)
            recvdata=tcpSock_cli.recv(BUFSIZE)
            print ">>%s" % recvdata
        except socket.error as e:
            break
