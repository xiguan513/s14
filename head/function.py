#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# #位置参数（必备参数）
# def fun(arg1,arg2,arg3):
#     print("arg1=",arg1)
#     print("arg2=",arg2)
#     print("arg3=",arg3)
#
# fun(1,2,3)
# fun(3,2,1)
#
# #关键字参数
# def fun1(arg1,arg2,arg3):
#     print("arg1=",arg1)
#     print("arg2=",arg2)
#     print("arg3=",arg3)
#
# fun1(arg1=1,arg3=3,arg2=2)
#
#
# #默认参数
# def fun2(arg1,arg2,arg3=3):
#     print("arg1=",arg1)
#     print("arg2=",arg2)
#     print("arg3=",arg3)
# fun2(1,2,4)
# fun2(1,2)
# fun2(arg3=4,arg2=2,arg1=1)
#
# #参数组
# def fun3(arg1,*args):
#     print("arg1=",arg1)
#     print("args",args)
# fun3(1,2,3,4,5)
# fun3(1)
#
# #参数字典
# def fun4(arg1,**kwargs):
#     print("arg1=",arg1)
#     print("kwargw=",kwargs)
# fun4(1,a=1,b="test")


"""代码中需要依赖到回调函数的使用(比如事件处理器、等待后台任务完成后的回调等)，
并且你还需要让回调函数拥有额外的状态值，以便在它的内部使用到。"""

# def apply_async(func,args,*,callback):
#     result=func(*args)
#     callback(result)
#
# def print_result(result):
#     print('Got:',result)
#
# def add(x,y):
#     return x+y
#
# apply_async(add,(2,3),callback=print_result)

#闭包函数 闭包是一类特殊的函数。如果一个函数定义在另一个函数的作用域中，并且函数中引用了外部函数的局部变量，那么这个函数就是一个闭包。

#
# def f():
#     n=1
#     def inner():
#         print("n=",n)
#     inner()
#     n='x'
#     inner()
#
# f()


# def f():
#     n=1
#     def inner():
#         nonlocal n
#         n='x'
#     print("n1=",n)
#     inner()
#     print("n2=",n)
#
# f()

#装饰器
import time

# def log(func):#传入一个函数（now）作为参数
#     def wrapper(*args,**kwargs):#配置闭包函数并配置不定长参数以便接收外部函数传入的值('song',26)
#         print(time.strftime('%Y%m%d%H%M%S'))
#         time.sleep(3)
#         print('call %s():' % func.__name__)
#         func_back=func(*args,**kwargs)#执行传入原始函数以及传入原始函数的参数now('song',26)
#         print(time.strftime('%Y%m%d%H%M%S'))
#         return func_back
#     return wrapper#返回执行结果的函数主体
#
# @log#等同于log(now('song','26'))
# def now(name,age):
#     return (name,age)

#now('song',26)
#print(now('song',26))


import time

def log(func):#传入一个函数（now）作为参数
    def wrapper(*args,**kwargs):#配置闭包函数并配置不定长参数以便接收外部函数传入的值('song',26)
        print(time.strftime('%Y%m%d%H%M%S'))
        time.sleep(3)
        print('call %s():' % func.__name__)
        func(*args,**kwargs)#执行传入原始函数以及传入原始函数的参数now('song',26)
        print(time.strftime('%Y%m%d%H%M%S'))

    return wrapper#返回执行结果的函数主体

@log#等同于log(now('song','26'))
def now(name,age):
    print (name,age)

now('song',26)
