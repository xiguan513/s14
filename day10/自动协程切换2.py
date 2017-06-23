#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""

默认情况下gevent 检测不到urlib和socket的io操作
所以不会进行切换
可以通过补丁包解决这个问题 monkey 补丁包


"""


import urllib
import gevent
import time
from gevent import monkey #补丁包

monkey.patch_all()#这个包的作用 把当前程序内部所有的io操作坐上标记（gevent.sleep）

def f(url):
    print "Get: %s " % url
    resp=urllib.urlopen(url)
    data=resp.read()
    print "Get file size %s" % len(data)

listurl=["http://www.cnblogs.com/alex3714/articles/5248247.html}","http://www.cnblogs.com/alex3714/articles/5830365.html","http://www.cnblogs.com/alex3714/articles/5230609.html"]


ynctime=time.time()
for i in listurl:
    f(i)
print "同步 done time %s" % (time.time()-ynctime)


ayrctime=time.time()
gevent.joinall([
    gevent.spawn(f,"http://www.cnblogs.com/alex3714/articles/5248247.html"),
    gevent.spawn(f,"http://www.cnblogs.com/alex3714/articles/5830365.html"),
    gevent.spawn(f,"http://www.cnblogs.com/alex3714/articles/5230609.html"),
])
print "异步 done time %s" % (time.time()-ayrctime)
