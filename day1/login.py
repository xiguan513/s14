#!/usr/bin/env python
# -*- coding: UTF-8 -*-

with open("passwd") as lock_file:
    lock_user=lock_file.readlines()

if [ user for user in lock_user if "song" in user.strip()  ]:
    print("111111")

import fileinput

for user in fileinput.input("passwd",backup=".bak",inplace=1):
    print(user.rstrip().replace('test',''))