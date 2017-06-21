#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
启动多进程并且在进程里面启动子线程

"""

import multiprocessing
import time,threading

def thread_run():
    print "输出当前线程id %s " % threading._get_ident()


def f(name):
    time.sleep(2)
    print "Hello", name
    t = threading.Thread(target=thread_run, )
    t.start()

if __name__=="__main__":

    for i in range(10):
        p=multiprocessing.Process(target=f,args=(i,))
        p.start()

