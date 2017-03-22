#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket_learn
from time import ctime


HOST='127.0.0.1'
PORT=8001
BUFSIZE=1024
ADDR=(HOST,PORT)



tcpser=socket_learn.socket(socket_learn.AF_INET, socket_learn.SOCK_STREAM)
tcpser.bind((ADDR))
tcpser.listen(5)

while True:
    print "waiting connect ......"
    conn,addr=tcpser.accept()
    print addr
    while True:
        fdata=conn.recv(BUFSIZE)
        if not fdata:
            break
        else:
            print '[%s] %s ' % (ctime(),fdata)
        sdata=conn.send('[%s] %s' % (ctime(),fdata))

    conn.close()
tcpser.close()
