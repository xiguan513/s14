#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket_learn

HOST='127.0.0.1'
PORT=8001
BUFSIZE=1024
ADDR=(HOST,PORT)

class Myclient():
    def __init__(self):
        self.tcpcli=socket_learn.socket(socket_learn.AF_INET, socket_learn.SOCK_STREAM)
        self.tcpcli.connect((ADDR))

        while True:
            sdata=raw_input(">")
            if not sdata:
                print "Not allowed to empty,please re-enter!"
                continue
            self.tcpcli.send(sdata)
            fdata=self.tcpcli.recv(BUFSIZE)
            print fdata
        self.tcpcli.close()

if __name__=="__main__":
    client=Myclient()