#!/usr/bin/env python
#-*- coding:utf-8 -*-

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print type(md5.hexdigest())
