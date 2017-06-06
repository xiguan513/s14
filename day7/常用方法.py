#!/usr/bin/env python
#-*- coding:utf-8 -*-


class C(object):

    def __new__(cls, *args, **kwargs):
        print "new"

    def __init__(self):
        self.name="ss"
        print "init"
    def __call__(self, *args, **kwargs):
        print "call"

    def __str__(self):
        return "This is str 方法"


#_new__方法接受的参数虽然也是和__init__一样，
# 但__init__是在类实例创建之后调用，而 __new__方法正是创建这个类实例的方法
# t=C()()#__call__如果两个括号表示执行call方法
t1=C()

print t1#__str__只返回字符串
