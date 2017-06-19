#!/usr/bin/env python
#-*- coding:utf-8 -*-

#守护线程配置

import threading
import time

def run(n):
    print "task %s" % n
    time.sleep(2)
    print "master %s" % n
    print "子线程", threading.current_thread()


thread_list=[]
start_time=time.time()
for i in range(50):
    t=threading.Thread(target=run,args=(i,))
    t.setDaemon(True)#配置子线程为守护线程
    t.start()

print "运行主线程执行时间，主线程执行完毕后直接退出，不等待守护子线程执行结果",time.time()-start_time
