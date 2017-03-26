#!/usr/bin/env python
#-*-coding:utf-8-*- 
#author: songbing


#生产者消费者模型
#单线程并行，异步epoll(nginx)
import time

def consumer(name):
    print("%s 准备吃包子了！" % name)
    while True:
        baozi=yield#返回空，中断程序直接返回值，并保存函数当前运行状态，提供函数返回点
        print("包子[%s]来了，被%s吃了！" % (baozi,name))

name="李阿攀"
c=consumer(name)
c.__next__()#恢复生成器,调用yield
c.send("韭菜馅")#给yield传值并恢复生成器继续运行


#next: 只调用yield，不给yield传值，并恢复生成器
#send: 调用yield的同时给yield传值，并恢复生成器



