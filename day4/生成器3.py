#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def thread1():
    for x in range(4):
        yield x

def thread2():
    for x in range(4,8):
        yield x

threads=[]
threads.append(thread1())
threads.append(thread2())
#print(threads)

import time


def run(threads):
    for t in threads:
        time.sleep(3)
        print(threads)
        try:
            print(t.__next__())
            #print("########################")
        except StopIteration:
            pass
        else:
            threads.append(t)
            #print(threads)

run(threads)