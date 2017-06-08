#!/usr/bin/env python
#-*- coding:utf-8 -*-



#md5 加密

import hashlib

m=hashlib.md5()

m.update("test")
m.update("agc")
#等同于m.update("testabc")
print m.hexdigest()


#如果数据量大可以分块多次调用update

#md5 解密


