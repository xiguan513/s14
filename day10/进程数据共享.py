#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
多进程间的数据共享
Manger默认已经加锁，不允许两个进程同时修改同一份数据

"""


from multiprocessing import Manager,Process
import os

def run(d,l):
    d[os.getpid()]=os.getpid()
    l.append(os.getpid())

p_list=[]

if __name__=="__main__":
    with Manager() as manager:
        d=manager.dict()#生成一个字典，可以在进程间共享
        l=manager.list(range(5))

        for i in range(10):
            p = Process(target=run, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()
        print d
        print l

