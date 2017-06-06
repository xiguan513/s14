#!/usr/bin/env python
#-*- coding:utf-8 -*-

#导入lib包下面的aa模块

mod=__import__("lib.aa")
ojb=mod.aa.C()
print ojb.name



#官方建议使用方法
import importlib
mod1=importlib.import_module('lib.aa')
obj=mod1.C()
print obj.name