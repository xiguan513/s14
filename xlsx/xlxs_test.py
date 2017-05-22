#!/usr/bin/evn python
# -*- coding:utf-8 -*-

import xlsxwriter

# 创建文件
work=xlsxwriter.Workbook("hello.xlsx")

#创建int表
workseet=work.add_worksheet("int")

title="abcdefgh"
data=[1,23,45,566,899,0,234,123]

for i,j in enumerate(title):
    print(i,j)
    point="A%d" % (i+1)
    workseet.write(point,j)

for i,j in enumerate(data):
    print(i,j)
    point="B%d" % (i+1)
    workseet.write(point,j)

work.close()
