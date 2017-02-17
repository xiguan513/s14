#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import fileinput

for line in fileinput.input("passwd",backup=".bak", inplace=1):
    print(line.rstrip().replace('song', ''))


def mininum(*values,clip=None):
    m=min(values)
    if clip is not None:
        m=clip if clip > m else m
    return m

print(mininum(1,5,2,-5,10))
print(mininum(1,5,2,-5,10,clip=0))