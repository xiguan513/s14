#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# f=open('b2c20170317.log','rt')
# print(f.read())
#
# with open('test.txt','a+t') as f:
#     print(f.read()+"ssss",file=f)

# with open('somefile','xt') as f:
#     f.write("Hwllo")

from tempfile import TemporaryFile
with TemporaryFile('w+t') as f:
    f.write('Hello, World\n')
    f.seek(0)
    data=f.read()
    print(data)
