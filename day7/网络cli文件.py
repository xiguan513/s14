#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
import os
import time

serfile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.75'
port = 9200
addr = (host, port)
serfile.connect(addr)
filename="2.zip"
file=open(filename,'ab')

filesize=serfile.recv(1024)
if "ready" in filesize:
    print "服务端发送：%s" % filesize
    filesize=filesize.split(" ")#获取服务端传送过来，原本文件的字节数
    serfile.send("yes")#告诉服务端可以开始传送文件
    time.sleep(5)
while True:
    data=serfile.recv(1024)
    if "done" in data:
        if int(filesize[1])-os.path.getsize(filename)<1024:#判断接收到的文件和传送的文件大小是否一致，如果不一致，重新再接收1024
            data = serfile.recv(1024)
            file.write(data)
        break
    else:
        print len(data)
        file.write(data)
else:
    file.close()
