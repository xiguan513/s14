#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Dog(object):
    def __init__(self,name):
        self.name=name

    @staticmethod
    def eat(cls):
        print(" eat " % (cls))

Dog.eat("包子")
