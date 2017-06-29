#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time

def log(func):
    ceshi="This is test data"
    def wrapper(*args,**kwargs):
        print time.strftime('%Y%m%d%H%M%S')
        time.sleep(2)
        func(*args,**kwargs)
        print ceshi
        print time.strftime('%Y%m%d%H%M%S')
    return wrapper

@log
def now(name,age):
    print "My name is %s and is %s years old!" % (name,age)


now("aa",24)