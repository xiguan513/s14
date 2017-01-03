#!/usr/bin/env python
# -*- coding: UTF-8 -*-

for i in  list(range(1,10)):
    print("\r")
    print(i,end=" ")
    for a in 'spam':
        print(a,end=" ")


# for i in list(range(1,10)):
#     for j in list(range(1,i+1)):
#         print("%dx%d=%d" % (j,i,j*i),end=" ")
#         if j==i:
#             print("\r")

