#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
普通ssh连接客户端连接
模拟ssh连接并执行命令

"""

import paramiko

#创建ssh对象
ssh=paramiko.SSHClient()

#允许连接在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接服务器
ssh.connect(hostname='192.168.0.151',port=22,username='song',password='1234@qwer')

#执行命令
stdin,stdout,stderr=ssh.exec_command('df')

#获取命令结果
resulu=stdout.read()


#关闭连接
ssh.close()



