#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket

HOST = 'localhost'  # The remote host
PORT = 5001  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    msg = raw_input(">>:")
    s.sendall(msg)
    data = s.recv(1024)
    # print(data)

    print('Received', repr(data))
s.close()