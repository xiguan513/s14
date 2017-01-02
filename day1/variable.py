#!/usr/bin/env python
#-*-coding:utf-8-*- 
#author: songbing

name="songbing"
_name="宋兵"
user_name=123
user1='test'
user_2name='ceshi'

name="songbing"
id(name)
name2=name
id(name2)
print()

print(name2,name)

name2="song"
id(name2)
print(name2,name)

username=input("Please input your name: ")
age=input("Please input your age: ")
print(type(age))
print("My name is %s and my age is %d" % (username,int(age)))
