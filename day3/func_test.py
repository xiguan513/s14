#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# def bar():
#     print 'in the bar'
#
# def foo(func):
#     res=func()
#     return res
# foo(bar)
#
# def foo(func):
#     return func
#
# print 'Function body is %s' % (foo(bar))
# print 'Function name is %s' % (foo(bar).func_name)
#
# foo(bar)()
# bar=foo(bar)
# bar()


def foo():
    def bar():
        print 'in the bar'
    bar()

foo()