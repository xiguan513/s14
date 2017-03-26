#!/usr/bin/env python
#-*-coding:utf-8-*- 
#author: songbing


import time

def decor(func):# 传入test1()函数体
    def waprr(*args,**kwargs):#接收test1()函数的参数传入进来
        start=time.time()
        func(*args,**kwargs)#运行docor传入的test函数体
        end=time.time()
        print("function runing time %f ,name: %s " % ((end-start),args[0]))
    return waprr#返回waprr的函数体即func的执行结果

@decor#  docor(test1())
def test1(name):
    time.sleep(3)
    print("This is test function! %s " % name)

name="song"
test1(name)



