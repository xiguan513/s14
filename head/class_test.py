#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#类继承
# class Person():
#     def __init__(self,name):
#         self.name=name
#
# class EmailPerson(Person):
#     def __init__(self,name,email):
#         super().__init__(name)
#         self.email=email
#
# bob=EmailPerson('bog','bob@mail.com')
# print(bob.email)
# print(bob.name)

#属性特性

class Duck():
    def __init__(self,input_name):
        self.hidden_name=input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self,input_name):
        print('inside the setter')
        self.hidden_name=input_name

    name=property(get_name,set_name)

fowl=Duck('Howard')
print(fowl.name)
# fowl.get_name()
# fowl.name="Daffy"
