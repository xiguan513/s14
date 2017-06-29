#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
接收端
消费者
"""

import pika
credentials=pika.PlainCredentials('admin','123456')
connect=pika.BlockingConnection(pika.ConnectionParameters('192.168.0.172',5672,'/',credentials))

channel=connect.channel()

channel.queue_declare(queue='hello')


#ch 生成的管道内存对象地址
#method 包含queue=hello 信息，对应哪个queue
def callback(ch,method,properties,body):
    print "Received %r" % body

#消费者信息
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print "Waiting for message.To exit press CTRL+C"

channel.start_consuming()