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
        recivedata=clnt.recv(1024)
        print "client send: %s" % recivedata
        while True:
            data=clnt.recv(1024).strip(" ")
            if not data:
                print "这是空数据，请重新输入！"
                break
            ip,port=address
            print 'Recieve data: %s %s' % (data.decode('utf-8'),ip)
            senddata=raw_input("发送数据:")
            clnt.send(senddata)
    except socket.error,e:
        print e

clnt.close()
sock.close()
