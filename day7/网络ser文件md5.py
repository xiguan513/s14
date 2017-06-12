#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
socket 文件传输

'''


import os
import socket
import hashlib

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
    recvdata=con.recv(bufsize)
    recvdata_list = recvdata.split(" ")
    if  "get" in recvdata:
        get_file_name=recvdata_list[1]
        if os.path.exists(get_file_name):
            filename = get_file_name
            filesize = str(os.path.getsize(get_file_name))
            text = "ready %s" % filesize
            con.send(text)
            print "客户端发送信息：%s" % recvdata  # 和客户端确认是否准备开始传送数据
            with open(filename, 'rb') as f:
                while True:
                    data = f.read(bufsize)
                    t = f.tell()  # 获取当前tell值
                    f.seek(t)  # 读取当前tell值以后的数据
                    if len(data) == 0:
                        con.send("done")
                        md5 = con.recv(1024)
                        if "md5" in md5:
                            con.send(m.hexdigest())
                            print "文件传输结束"
                        break
                    else:
                        con.sendall(data)
                        m.update(data)
                        print len(data)
        else:
            print "文件不存在"
            con.send("file not found!")

