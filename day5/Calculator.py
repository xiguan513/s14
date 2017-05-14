#!/usr/bin/env python
#-*- coding: utf-8 -*-


import re
text='1-2*((60-30*(9-2*5/3+7/3*99/4*2+10*8/14+1))-(-4*3)/(16-3*2))'
print text
print "+++++++++++++++++++++++++++++++++++"

k1=re.compile(r'\([^()]*\)')#取出去两个括号之间不包含（）的任意数据
a=k1.search(text).group()
print a
for i in re.split(r'[\+\-]',a):
    if '*' in i or '/' in i:
        i=i.strip(')')
        i=i.strip('(')

        print i

