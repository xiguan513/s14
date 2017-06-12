#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
import os
import time
import hashlib

m1=hashlib.md5()


serfile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.75'
port = 9200
addr = (host, port)
serfile.connect(addr)
filename="5.rar"
file=open(filename,'ab')
get_file=raw_input("Please input filename: ").strip(" ")#获取输出文件名

serfile.send(get_file)#发送需要获取的文件信息
filesize=serfile.recv(1024)#接收服务端的确认信息
if "ready" in filesize:
    print "服务端原始文件size：%s" % filesize
    filesize=filesize.split(" ")#获取服务端传送过来，原本文件的字节数
    while True:
        surplus_file_size = int(filesize[1]) - int(os.path.getsize(filename))
        print "剩余文件大小",surplus_file_size
        if surplus_file_size < 1024:  # 判断接收到的文件和传送的文件大小是否一致，如果不一致，重新再接收剩余的部分
            bufsize=surplus_file_size
        else:
            bufsize=1024
        data = serfile.recv(bufsize)
        file.write(data)
        file.flush()

    print "原始文件size: %d  已接收文件size: %d" % (int(filesize[1]),os.path.getsize(filename))


elif "not" in filesize:
    print "文件没有找到"