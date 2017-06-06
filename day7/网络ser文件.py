#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
socket 文件传输

'''


import os
import socket

serfile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 9200
bufsize=1024
addr = (host, port)
serfile.bind(addr)
serfile.listen(5)
filename="1.zip"
filesize=str(os.path.getsize(filename))
text="ready %s" % filesize
while True:
    con,add = serfile.accept()
    con.send(text)
    recvdata=con.recv(bufsize)
    if  "yes" in recvdata:
        print "客户端发送信息：%s" % recvdata#和客户端确认是否准备开始传送数据
        with open(filename,'rb') as f:
            while True:
                data=f.read(bufsize)
                t=f.tell()#获取当前tell值
                f.seek(t)#读取当前tell值以后的数据
                if len(data)==0:
                    print "文件传输结束"
                    con.send("done")
                    break
                else:
                    con.sendall(data)
