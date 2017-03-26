#!/usr/bin/env python
#-*-coding:utf-8-*- 
#author: songbing


#生产者消费者模型
#单线程并行，异步epoll(nginx)
import time

def consumer(name):
    print("%s 准备吃包子了！" % name)
    while True:
        baozi=yield#返回空
        print("包子[%s]来了，被%s吃了！" % (baozi,name))

name="李阿攀"
c=consumer(name)
c.__next__()#恢复生成器
c.send("韭菜馅")#给yield传值并恢复生成器



