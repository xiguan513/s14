#!/usr/bin/env python
#-*- coding:utf-8 -*-

a=[1,2,3]
b={}
try:
    print name
    a[3]
    print b["aa"]
except IndexError as mes:
    print mes
except NameError as mes:
    print mes
except Exception as mes:#抓取所有异常处理
    print mes
else:#try语句没有错误的时候执行
    print "没有错误"
finally:#不管try语句是否有错误，都执行
    print "有没有错误都执行"


