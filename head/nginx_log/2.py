#!/usr/bin/env python
# -*- coding: UTF-8 -*-

with open('1','r') as f:
    for i in f.readlines():
        if i.startswith('unknown,'):
            i=i.replace('unknown,', '')
            print i