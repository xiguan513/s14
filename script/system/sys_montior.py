#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import psutil

#psutil 输出的单位为字节
"""
单位换算
1 Byte = 8 Bits

1 KB = 1024 Bytes

1 MB = 1024 KB

1 GB = 1024 MB
"""

#CPU信息

print "获取CPU全部信息"
print psutil.cpu_times()
print "获取CPU物理个数"
print psutil.cpu_count(logical=False)
print "获取CPU逻辑个数"
print psutil.cpu_count()


#内存信息
#linux系统内存利用率信息涉及to-tal(内存总数)，used(以使用内存)，free(空闲内存)，buffers(缓冲使用数)

mem=psutil.virtual_memory()
print "总内存"
print mem.total/1024/1024
print "已使用内存"
print mem.used/1024/1024

#print "linux 内存使用情况：" ,mem.free/1024/1024+mem.cached/1024/1024


print psutil.disk_io_counters()
