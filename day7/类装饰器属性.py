#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    # @price.deltter
    # def price(self, value):
    #     del self.original_price

    def __call__(self, *args, **kwargs):
        print ("running call %s %s" % (args,kwargs))

    def __str__(self):#永远返回一个字符串，可以返回需要类定义的信息
        return "%s" % self.discount


obj = Goods()
print obj.price         # 获取商品价格
obj.price = 200   # 修改商品原价
print obj.price
#del obj.price     # 删除商品原价

#__call__方法
obj()
obj(1,2,3,name=333)

#__str__方法
print obj


#__dict__
print obj.__dict__#打印所有实例属性，不包括类属性
print Goods.__dict__#打印类里面所有的属性，不包括实例属性