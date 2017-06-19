#!/usr/bin/env python
#-*- coding:utf-8 -*-


#根据红灯绿灯状态，判断汽车是否可以通过

#红绿灯线程

import threading
import time

event=threading.Event()


def lighter():
    count = 0
    event.set()#设置标志位
    while True:
        if count>10 and count < 15:#设置绿灯参数，
            event.clear()#清除标志位
            print "\033[41mred ligth runing...\033[0m"
        elif count>15:#设置红灯参数
            count = 0#清除计数器
            event.set()#设置标志位
            print count
        else:#显示当前状态为绿灯
            print "\033[42mgreen ligth runing....\033[0m"
        time.sleep(1)
        print "计数",count
        count+=1

def car(name):
    while True:
        if event.is_set():#查看标志位状态信息
            print "%s runing......" % name
            time.sleep(1)
        else:
            print "%s waiting red light....." % name
            event.wait()



if __name__=="__main__":
    light=threading.Thread(target=lighter,)
    light.start()
    car1=threading.Thread(target=car,args=("tst",))
    car1.start()