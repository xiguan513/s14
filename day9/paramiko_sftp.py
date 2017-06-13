#!/usr/bin/env python
#-*- coding:utf-8 -*-

import paramiko

private_key=paramiko.RSAKey.from_private_key_file('id_rda')

transport=paramiko.Transport(('192.168.0.151',22))
transport.connect(username='song',pkey=private_key)

sftp=paramiko.SFTPClient.from_transport(transport)

#上传将本地的1.txt 上传到服务器并命名2.txt

sftp.put('1.txt','2.txt')

#下载将服务器2.txt 下载到本地并命名1.txt

sftp.get('2.txt','1.txt')

#关闭连接
transport.close()