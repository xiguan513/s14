#!/usr/bin/env python
#-*- coding:utf-8 -*-


line="""
192.168.0.74 - - [29/Jun/2017:18:40:37 +0800] "GET /index/tripList?type=3 HTTP/1.1" 200  GET　991 "http://test.lvph.cn/" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0" "-"test.lvph.cn 200 192.168.1.221:80 2.684 2.684"-"
"""

import re


a=re.compile(r'{}'.format("GET"),re.I)


# if re.findall(a,line):
#     res = re.sub(a,r'<font color="red">{}</font>'.format("GET"),line)
#     print res
# else:
#     print "222222222"
