#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import fileinput

for line in fileinput.input("passwd",backup=".bak", inplace=1):
    print(line.rstrip().replace('song', ''))
