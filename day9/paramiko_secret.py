#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
秘钥ssh连接客户端连接
模拟ssh连接并执行命令

"""

import paramiko

#指定秘钥位置
private_key=paramiko.RSAKey.from_private_key_file('id_rda')

#创建ssh对象
ssh=paramiko.SSHClient()

#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接服务器
ssh.connect(hostname='192.168.0.151',port=22,username='song',pkey=private_key)

#执行命令stdin基本输入，stdout基本输出，stderr错误信息
stdin,stdout,stderr=ssh.exec_command('df')

#获取命令结果
result=stdout.read()

#关闭连接
ssh.close()