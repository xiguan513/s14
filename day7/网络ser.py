#!/usr/bin/env python
#-*- coding:utf-8 -*-


import socket

#实例化服务器端socket对象方法
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST='0.0.0.0'
PORT=9200
addr=(HOST,PORT)
sock.bind(addr)#元组
sock.listen(5)

while True:
    try:
        clnt, address = sock.accept()
        while True:
            data=clnt.recv(1024).strip()
            if not data:
                break
            ip,port=address
            print 'Recieve data: %s %s %s' % (data,ip,port)
            senddata=data.upper()
            clnt.send(senddata)
    except socket.error,e:
        print e

clnt.close()
sock.close()
