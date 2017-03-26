#!/usr/bin/env python
#-*-coding:utf-8-*- 
#author: songbing

def fib(max):
    n,a,b=0,0,1
    while n < max:
        #print(b)
        yield b#中断程序直接返回值，并保存函数当前运行状态，提供函数返回点
        a,b=b,a+b
        n+=1
    return 'done'

b=fib(10)

while True:
    try:
        f=b.__next__()
        print('f:',f)
    except StopIteration as e:
        print(e)
        break

