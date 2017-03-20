#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
nametime=time.strftime('%Y-%m-%d',time.localtime(time.time()))

print(nametime)
file=open(nametime+"1.txt", 'a+' )