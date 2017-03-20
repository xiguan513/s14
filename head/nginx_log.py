#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#nginx日志过滤规cdn等代理ip，规范格式

import re
import sys
import time

reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')

log_file='b2c20170317.log'
#log_file=sys.argv[1]

f=open(log_file)
nametime=time.strftime('%Y%m%d',time.localtime(time.time()))
f1=open(nametime+"nginx.log","a+")


#for 循环 if 模式
# for i in f.readlines():
#     if reip.findall(i):
#         disk_ip = reip.findall(i)
#         i=i.split(" ")
#         if reip.findall(i[1]):
#             i.pop(1)
#             if reip.findall(i[1]):
#                 i.pop(1)
#                 if reip.findall(i[1]):
#                     i.pop(1)
#         i[0]=i[0].replace(",","")
#         i=" ".join(i)
#         f1.write(i)
#
# f.close()
# f1.close()


#迭代模式
for i in f.readlines():
    if reip.findall(i):
        disk_ip = reip.findall(i)
        i=i.split(" ")
        def ippop(ip):
            if reip.findall(ip[1]):
                ip[0] = ip[0].replace(",", "")
                ip.pop(1)
                ippop(ip)
        ippop(i)
        ip = " ".join(i)
        f1.write(ip)
f.close()
f1.close()