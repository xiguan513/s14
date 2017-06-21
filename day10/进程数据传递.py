#!/usr/bin/env python
#-*- coding:utf-8 -*-


import multiprocessing
from multiprocessing import Queue #进程Queue

#import Queue#线程Queue 在python3 中 import queue


def run(qq):
    qq.put("This is test")

if __name__=="__main__":
    q=Queue()
    p=multiprocessing.Process(target=run,args=(q,))#创建子进程并把队列q作为参数传递给子进程
    p.start()#启动进程
    print q.get()