#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Myclass:
    name='This is class variable'
    n='This test n '
    def __init__(self,name):
        self.name=name

    def say(self):
        print "show %s name " % self.name

    def __del__(self):
        print "析构函数"

# Myclass.n="修该类变量"
#
# a=Myclass("song")
# a.say()
# print a.name
# a.n="更该实力a变量"
# print '类变量N',a.n
#
#
# print "+++++++++++++++++++++++++"
# a1=Myclass("bing")
# a1.say()
# print a1.name
# print "类变量N",a1.n

b=Myclass("song")
b.say()