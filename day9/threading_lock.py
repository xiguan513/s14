#!/usr/bin/env python
#-*- coding:utf-8 -*-

#用户级别锁（互斥锁）

import threading
import time

num=0
def run(n):
    lock.acquire()#申请锁
    global num
    num+=1
    lock.release()#释放锁

lock=threading.Lock()
for i in range(5000):
    t=threading.Thread(target=run,args=(i,))
    t.start()

print "num %s" % num



