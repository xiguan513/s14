#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket

sockcli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST='192.168.1.75'
PORT=9200
addr=(HOST,PORT)
sockcli.connect(addr)

while True:
    senddata=raw_input("send data:")
    if len(senddata)==0:continue
    sockcli.send(senddata)
    revedata=sockcli.recv(1024)
    print revedata
