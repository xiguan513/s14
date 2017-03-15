#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#实现读取列表中所有内容






movies=[
    "The Holy Grail",1975,
    "Terry Jones & Terry Gilliam",91,
    ["Graham Chapman",
     ["Michael Plain","John Clessse","Terry Gilliam","Eric Idle","Terry Jones"]
     ]
]
#print(movies[4][1][3])

#for 循环方式读取
for each_item in movies:
    #print(each_item)
    if isinstance(each_item,list):
        for each_item1 in each_item:
            if isinstance(each_item1,list):
                for each_item2 in each_item1:
                    print(each_item2)
            else:
                print(each_item1)

    else:
        print(each_item)

print("========================================================")


#函数递归方式读取
def print_lol(mov):
    for each_item in mov:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(movies)

