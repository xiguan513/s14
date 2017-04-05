#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# def scope_test():
#     def do_local():#闭包函数修改全局变量值，但是对全局不生效，只在闭包函数内生效
#         spam="local spam"
#         print("This is do_local:",spam)
#     def do_nonlocal():#闭包函数修改全局变量值，对本闭包函数生效，以及上层函数生效，函数级别。最里层作用域之外的变量
#         nonlocal spam
#         spam="nonlocal spam"
#     def do_global():#闭包函数修改变量为全局变量,块级别
#         global spam
#         spam="global spam"
#         print("This is do_global:",spam)
#
#     spam="test spam"
#     do_local()
#     print("After do_local assignment:",spam)
#     do_nonlocal()
#     print("After nonlocal assignment:",spam)
#     do_global()
#     print("After global assignment:",spam)
#
# spam="out spam"
# scope_test()
# print("In global scope:",spam)


def a():
    def b():
        nonlocal m
        m=3
    def c():
        print("c:",m)
    def d():
        global m
        m=4
    m=1
    b()
    c()
    d()
    print("a:",m)

m=0
a()
print("m:",m)



