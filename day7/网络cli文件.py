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
filename="2.rar"
file=open(filename,'ab')

get_file=raw_input("Please input filename: ").strip(" ")

recv_file_name=serfile.send(get_file)

filesize=serfile.recv(1024)
if "ready" in filesize:
    print "服务端原始文件size：%s" % filesize
    filesize=filesize.split(" ")#获取服务端传送过来，原本文件的字节数
    serfile.send("yes")#告诉服务端可以开始传送文件
    time.sleep(5)
    while True:
        data=serfile.recv(1024)
        if "done" in data:
            print "done 以后的数据",data
            break
        else:
            print len(data)
            file.write(data)

    file.close()
    print "原始文件size: %d  已接收文件size: %d" % (int(filesize[1]),os.path.getsize(filename))
elif "not" in filesize:
    print "文件没有找到"