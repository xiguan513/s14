#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket


HOST="127.0.0.1"
PORT=9002
SIZE=1024
ADDR=(HOST,PORT)

tcpcliSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpcliSock.connect((ADDR))

while True:
    recvdata=tcpcliSock.recv(SIZE)
    senddata="客户端发送数据"
    tcpcliSock.sendall(senddata)
    print recvdata
    while True:
        rawdata=raw_input(">>")
        tcpcliSock.sendall(rawdata)
        rawrevedata=tcpcliSock.recv(1024)
        print rawrevedata