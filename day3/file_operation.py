#!/usr/bin/env python
#-*-coding:utf-8-*- 
#author: songbing

file_name="file_example"
f=open(file_name,encoding='utf-8')#打开文件句柄
#print(f.read())

#循环读取文件
# for line in f:
#     print(line.strip())

#直接读取文件f的方式比readlines要高效readlines读取所有内容到内存中，f的方式在内存中只读取一行内容
for line1 in f.readlines():
    print(line1)
f.close()
