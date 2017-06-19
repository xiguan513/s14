#!/usr/bin/env python
#-*- coding:utf-8 -*-


import threading
import time
import Queue



def producer(name):
    count=1
    while True:
        q.put(count)
        print "%s 生产了第 %s 个馒头" % (name,count)
        count+=1
        time.sleep(0.5)

def consumer(name):
    while True:
        print "%s 吃了第 %d 个馒头" % (name,q.get())
        time.sleep(1)



if __name__=="__main__":
    q=Queue.Queue(maxsize=10)

    p=threading.Thread(target=producer,args=("食堂",))
    c=threading.Thread(target=consumer,args=("食客222222",))
    c1=threading.Thread(target=consumer,args=("食客333333",))
    p.start()
    c.start()
    c1.start()
