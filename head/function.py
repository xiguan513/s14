#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# def avg(first,*rest):
#     print("first",first)
#     print("rest",rest)
#     print("sum",sum(rest))
#     print("len",len(rest))
#     return (first+sum(rest))/(1+len(rest))
# print(avg(1,2,3,4))


# def recv(maxsize,*,block):
#     print(maxsize)
#     print(block)
#
# recv(1024,block=True)
#
# def mininum(*values,clip):
#     print(values)
#     print(clip)
# mininum(1,5,2,-6,4,clip=12)


"""代码中需要依赖到回调函数的使用(比如事件处理器、等待后台任务完成后的回调等)，
并且你还需要让回调函数拥有额外的状态值，以便在它的内部使用到。"""

def apply_async(func,args,*,callback):
    result=func(*args)
    callback(result)

def print_result(result):
    print('Got:',result)

def add(x,y):
    return x+y

apply_async(add,(2,3),callback=print_result)


