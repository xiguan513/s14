#!/usr/bin/env python
#-*-coding:utf-8-*- 
#author: songbing


import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield
       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

# c = consumer("ChenRonghua")
# c.__next__()

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("%s开始准备做包子啦!" % name)
    for i in range(10):
        time.sleep(1)
        print("做了1个包子,分两半!")
        c.send(i)
        c2.send(i)

producer("李")