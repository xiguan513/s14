#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
send 发送端
生产者

"""


import pika

credentials=pika.PlainCredentials('admin','123456')
connection=pika.BlockingConnection(pika.ConnectionParameters('192.168.0.172',5672,'/',credentials)) #建立连接

channel=connection.channel() #声明管道

#声明queue
channel.queue_devlare(queue='hello')

channel.basic_publish(exchange="",
                      routing_key="hello",
                      body="hello world!")

connection.close()