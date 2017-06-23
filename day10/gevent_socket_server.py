#!/usr/bin/env python
#-*- coding:utf-8 -*-


import socket
import gevent

from gevent import monkey

monkey.patch_all()


host='localhost'
port=5001
ADDR=(host,port)

def server():
    ser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ser.bind(ADDR)
    ser.listen(100)

    while True:
        cli,addr=ser.accept()
        gevent.spawn(handle_request,cli)#每过来一个新的连接就创建一个新的协程

def handle_request(conn):
    try:
        while True:
            data=conn.recv(1024)
            print "Recv: %s " % data
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)
    except Exception as ex:
        print ex
    finally:
        conn.close()

if __name__=="__main__":
    server()

