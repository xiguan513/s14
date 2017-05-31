#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Myclass(object):
    n='This test n '#类属性
    def __init__(self,name):#析构函数
        self.name=name#实例属性
        self.__age=12#私有属性

    def say(self):#实例方法
        return "show %s name ,age is %s" % (self.name,self.__age)

    def __eat(self):#私有方法
        return "ceshi"

    # def __del__(self):
    #     print "析构函数"

Myclass.n="修该类属性" #类属性
Myclass.name="修该name属性" #类属性
print "类属性",Myclass.name#类属性
a=Myclass("song")
print '类属性a的n属性:',a.n
b=Myclass("bing")
print '类属性b的n属性:',b.n

print "实例a方法say:" ,a.say()#实例方法
print "实例b方法say:" ,b.say()#实例方法
print "实例属性name:",a.name #实例属性
a.n="更该实例a的n属性"
print '类属性a的n属性:',a.n
print '类属性b的n属性:',b.n

