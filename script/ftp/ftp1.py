#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from ftplib import FTP

f=FTP()
f.connect('127.0.0.1','29')
f.login('song','123456')
f.pwd()
f.dir()
f.quit()

