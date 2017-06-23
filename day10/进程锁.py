#!/usr/bin/env python
#-*- coding:utf-8 -*-


from multiprocessing import Process,Lock

def run(l,i):
    l.acquire()
    try:
        print "hello word",i
    finally:
        l.release()


if __name__=="__main__":
    lock=Lock()
    for i in range(10):
        p=Process(target=run,args=(lock,i))
        p.start()
