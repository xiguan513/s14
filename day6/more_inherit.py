#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Person(object):
    def __init__(self,name,age,*args):
        self.name=name
        self.age=age
        super(Person, self).__init__(*args)
    def say(self):
        print("My name is %s  and I am %s years old" % (self.name,self.age))

class Boy(object):
    def __init__(self,sex):
        self.sex=sex

#继承两个父类参数不同的情况，旧式类继承
class student(Person,Boy):
    def __init__(self,name,age,sex,curriculum):
        Person.__init__(self,name,age)
        Boy.__init__(self,sex)
        self.curriculum=curriculum

    def status(self):
        print("My name is %s and i am %s years old ,i am a %s" % (self.name,self.age,self.sex))


#继承两个父类参数不同的情况，新式类继承
class teacher(Person,Boy):
    def __init__(self,name,age,sex,sarry,*args):
        self.sarry=sarry
        super(teacher,self).__init__(name,age,sex,*args)

    def status(self):
        print("My name is %s and i am %s years old ,i am a %s ..%s" % (self.name,self.age,self.sex,self.sarry))

# l=student('song',27,'man','python')
# l.status()

t=teacher("li",28,'woman',10000)
t.status()