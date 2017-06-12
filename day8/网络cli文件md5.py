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
filename="3.rar"
file=open(filename,'ab')

get_file=raw_input("Please input filename: ").strip(" ")#获取输出文件名

recv_file_name=serfile.send(get_file)#发送需要获取的文件信息

filesize=serfile.recv(1024)
if "ready" in filesize:
    print "服务端原始文件size：%s" % filesize
    filesize=filesize.split(" ")#获取服务端传送过来，原本文件的字节数
    time.sleep(5)
    while True:
        data=serfile.recv(1024)
        if "done" in data:
            serfile.send("md5")
            md5 = serfile.recv(1024)
            if md5==m1.hexdigest():
                print "文件一样\n",
            break
        else:
            print len(data)
            file.write(data)
            m1.update(data)
    file.close()
    print "原始文件size: %d  已接收文件size: %d" % (int(filesize[1]),os.path.getsize(filename))


elif "not" in filesize:
    print "文件没有找到"