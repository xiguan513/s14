#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""

并且通过此方法调用
if __name__ == '__main__':
    
"""

from multiprocessing import Pool,Process
import time
import os

def foo(i):
    time.sleep(1)
    print "foo process name %s and process id %s" % (i,os.getpid())
    return os.getpid()


def bar(arg):
    print os.getpid()
    print "bar",arg

if __name__ == '__main__':
    pool=Pool(5)#运行进程池同时放入5个进程
    for i in range(10):
        #pool.apply(func=foo,args=(i,))#创建进程,串行
        #pool.apply_async(func=foo,args=(i,))#创建进程,并行
        pool.apply_async(func=foo,args=(i,),callback=bar)#创建进程,并行,callback回调的意思，表示必须执行完成foo以后调用bar

        """
        回调函数bar 必须带一个参数
        并且这个参数默认接收foo函数执行完成后return返回的结果
        而且bar函数是由主进程调用的回调
        """

    print "end",os.getpid()
    pool.close()#关闭进程池
    pool.join()#进程池中进程结束以后再关闭,如果注释此项，会直接关闭进程池，不等里面的进程是否执行完毕