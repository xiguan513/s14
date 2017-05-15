#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from socket import *
from IPy import IP

ip=IP('192.168.0.0/22')

def portScanner(host,port):
    s = socket(AF_INET,SOCK_STREAM)
    result = s.connect_ex((host,port))
    if result==0:
        print('IP地址：%s     端口号： %d open' % (host,port))
        s.close()

def main():
    setdefaulttimeout(1)
    for i in ip:
        i=str(i)
        portScanner(i,445)
        portScanner(i,135)

if __name__ == '__main__':
    main()

