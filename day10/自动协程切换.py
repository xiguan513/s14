#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
遇到io操作就切换
自动切换

"""

import gevent


def fun1():
    print 12
    gevent.sleep(4)
    print 34

def fun2():
    print 56
    gevent.sleep(3)
    print 78

def fun3():
    print 22
    gevent.sleep(1)
    print 23

gevent.joinall([
    gevent.spawn(fun1),
    gevent.spawn(fun2),
    gevent.spawn(fun3),
]) #启动协程，并自动切换，遇到sleep自动切换协程