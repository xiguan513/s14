#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
遇到io操作就切换
手动切换

"""

from greenlet import greenlet


def fun1():
    print 12
    gr2.switch()
    print 34
    gr2.switch()

def fun2():
    print 56
    gr1.switch()
    print 78

gr1=greenlet(fun1)#启动协程
gr2=greenlet(fun2)
gr1.switch()#手动切换协程