#!/usr/bin/env python
#-*- coding:utf-8 -*-

#信号量（多把锁）
#连接池同一时间只能有5把锁

import threading,time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print "run the thread: %s\n" %n
    semaphore.release()


if __name__=="__main__":
    num=0
    semaphore=threading.BoundedSemaphore(5)
    for i in range(20):
        t=threading.Thread(target=run,args=(i,))
        t.start()

while threading.active_count() !=1:
    pass
else:
    print "----------all threads done------"
