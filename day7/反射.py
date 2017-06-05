#!/usr/bin/env python
#-*- coding:utf-8 -*-

class fan(object):
    name='xiaohua'
    def run(self):
        return "Hello World"


if __name__=="__main__":
    t=fan()
    if hasattr(t,"name"):
        print "判断对象有name属性"

    if hasattr(t,"run"):
        print "判断对象有run方法"

    if hasattr(t,"age"):
        pass
    else:
        print "对象中没有age方法或者属性"

    getname=getattr(t,"name")#调用类的属性，存在就打印
    print getname

    getrun=getattr(t,"run")#调用类的方法，存在就打印内存地址，获取方法加上（）
    print getrun()

    #getage = getattr(t, "age")#调用一个不存在的属性，报错
    getage=getattr(t,"age","18")#调用一个不存在的属性，可以给一个默认值
    print getage


    #判断属性sex是否存在，如果不存，使用setattr添加属性，在使用getattr获取属性
    if hasattr(t,"sex"):
        pass
    else:
        setattr(t,"sex","男")
        if hasattr(t,"sex"):
            print "添加属性sex"
        getsex=getattr(t,"sex")
        print getsex


    # 判断方法say是否存在，如果不存，使用setattr添加方法，在使用getattr获取方法
    # sanfan方法名字，say对应的添加的新函数方法 t.sayfan=say()
    def say(self,age):
        print "%s在说话,添加的说话方法 %s" % (self.name,age)
    if hasattr(t,"say"):
        pass
    else:
        setattr(t,"sayfan",say)
        getfan = getattr(t,"sayfan")
        getfan(t,22)

    '''
    不加参数的方法
    def say(self):
        print "%s在说话,添加的说话方法 %s" % (self.name)


    if hasattr(t, "say"):
        pass
    else:
        setattr(t, "sayfan", say)
        getfan = getattr(t, "sayfan")
        getfan(t)
    '''

    # 删除对象的属性或者方法
    # if hasattr(t,"name"):
    #     delattr(t,"name")
    #     getname=getattr(t,"name")
    #     print getname


try:
    pass
except Exception as e:
    pass
