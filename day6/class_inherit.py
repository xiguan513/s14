#!/usr/bin/env python
#-*- coding: utf-8 -*-


class People(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def eat(self):
        print "eat something..."

    def say(self):
        print "Hello !My name is %s " % self.name

class status(People):
    def __init__(self,name,age,sex,score):
        People.__init__(self,name,age,sex)
        self.__score=score

    def scores(self):
        #People.say(self)
        print "%s is %s  score is %s" % (self.name,self.sex,self.__score)

class tearch(People):
    def __init__(self,name,age,sex,money):
        super(tearch,self).__init__(name,age,sex)
        self.money=money

    def moneys(self):
        print "My name is %s money %s  sex is %s" % (self.name,self.money,self.sex)

# a=status("li","27","女",89)
# a.scores()

b=tearch("song",27,"男",100)
b.moneys()