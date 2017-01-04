#!/usr/bin/env python
# -*- coding: UTF-8 -*-

with open("passwd") as lock_file:
    for line in lock_file.readlines():
        if "admin" in line.strip():
            print("111111")