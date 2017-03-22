#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import ftplib
import os
import socket


HOST='127.0.0.1'
FILE='1.gz'
bufsize=1024
file_handle=open(FILE,'wb').write
print file_handle

def main():
    try:
        f=ftplib.FTP() #实例化对象
    except (socket.error, socket.gaierror) as e:
        print 'error: cannont reach "%s"' % HOST
        return
    print '*** Connected to host "%s"' % HOST

    try:
        f.connect(HOST,21)
        f.login("song","123456") #登录接口，如果是非21端口需要先使用f.connect('127.0.0.1','port')登录
        f.dir()#显示目录内容
    except ftplib.error_perm:
        print 'Eorror: canont login "anonymous"'
        f.quit()
        return
    print '*** logged is as "song"'


    try:
        f.retrbinary('RETR %s' % (FILE),file_handle,bufsize) #下载文件 上传文件ftp.storbinaly("STOR filename.txt",file_handel,bufsize)
    except ftplib.error_perm:
        print 'Error: canoncet read file "%s"' % FILE
        os.unlink(FILE)
    else:
        print '*** Downloadwd "%s" to CWD' % FILE
    f.quit()


if __name__=="__main__":
    main()