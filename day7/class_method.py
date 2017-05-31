#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Dog(object):
    age=12
    def __init__(self,name):
        self.name=name

    @staticmethod
    def eat(thing):#静态方法变成一普通函数
        print(" eat %s " % (thing) )

    @classmethod
    def say(cls):#类方法
        print("my age is %s " % cls.age)

    @property
    def price(self):
        print "@property"

    @price.setter
    def price(self,value):
        self.name=value

    @price.deleter
    def price(self):
        print "@price.deleter"

Dog.eat("包子")
d=Dog("test")
print "我是实例方法调用的",d.say()
print "我是类方法调用的",Dog.say()

d.price#实例属性
d.price="这是实例属性，并且修改实例属性的值"
print d.name


