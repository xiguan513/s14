#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import socket

HOST='127.0.0.1'
PORT=8002
BUFSIZE=1024
ADDR=(HOST,PORT)

class Myclient():
    def __init__(self):
        self.tcpcli=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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