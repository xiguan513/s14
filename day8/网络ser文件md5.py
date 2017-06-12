#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
socket 文件传输

'''


import os
import socket
import hashlib
import time

m=hashlib.md5()

serfile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 9200
bufsize=1024
addr = (host, port)
serfile.bind(addr)
serfile.listen(5)

while True:
    print "等待传输文件"
    con,add = serfile.accept()
    recvdata=con.recv(bufsize)#接收客户端传送的文件名以及下载命令
    recvdata_list = recvdata.split(" ")
    print recvdata_list
    if  "get" in recvdata_list[0]:#判断客户端是否get文件
        get_file_name=recvdata_list[1]#获取客户端需要的文件名
        if os.path.exists(get_file_name):#判断本地文件是否存在
            filesize = str(os.path.getsize(get_file_name))#获取文件大小
            text = "ready %s" % filesize
            con.send(text)#发送客户端确认信息
            print "客户端发送信息：%s" % recvdata  # 和客户端确认是否准备开始传送数据
            with open(get_file_name, 'rb') as f:
                while True:
                    data = f.read(bufsize)
                    t = f.tell()  # 获取当前tell值
                    f.seek(t)  #读取当前tell值以后的数据
                    if len(data) == 0:
                        print len(data)
                        con.send("done")
                        break
                    else:
                        con.send(data)
                        print len(data)
                f.seek(0)
            print "结束文件"
            f.close()
        else:
            print "文件不存在"
            con.send("file not found!")

