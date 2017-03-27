#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def gen():
    for x in range(4):
        tmp=yield x
        if tmp=="hello":
            print('world')


try:
    g=gen()
    print(type(g))

    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())

    print(g.send('hello'))
except StopIteration as e:
    print(e)