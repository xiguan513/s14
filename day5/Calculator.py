#!/usr/bin/env python
#-*- coding: utf-8 -*-


import re
text='1-2*((60-30*(9-2*5*4/3+7/3*99/4*2+10*8/14+1))-(-4*3)/(16-3*2))'
print text
print "+++++++++++++++++++++++++++++++++++"


def n_k(text):
    #先取出最里面的括号
    k1=re.compile(r'\([^()]*\)')#取出去两个括号之间不包含（）的任意数据
    a=k1.search(text).group()
    for j_j in re.split(r'[+-]',a):
        if '*' in j_j or '/' in j_j:
            yield j_j


def chen_chu(test):
    for i in test:
        print i




if __name__=="__main__":
    chen_chu(n_k(text))











