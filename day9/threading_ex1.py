#!/usr/bin/env python
#-*- coding:utf-8 -*-


#基础线程配置

import threading
import time

def run(n):
    print "task %s" % n
    time.sleep(2)
    print "master %s" % n
    print "子线程", threading.current_thread()

# t1=threading.Thread(target=run,args=("t1",))
# t2=threading.Thread(target=run,args=("t2",))
#
# t1.start()
# t2.start()


"""
下面代码执行结果显示，主线程执行结束以后不等待子线程执行结束，直接往下执行代码
线程里面程序join等待子线程执行以后继续执行后续线程
"""
thread_list=[]
start_time=time.time()
for i in range(50):
    t=threading.Thread(target=run,args=(i,))
    t.start()
    thread_list.append(t)#为了不阻塞后面线程的启动，

for i in thread_list:
    i.join()#循环线程实例列表，等待所有线程执行完毕
print "查看当前的进程id,以及当前活动的线程个数",threading.current_thread(),threading.active_count()#查看当前的进程id,以及当前活动的线程个数


print "运行时间",time.time()-start_time


