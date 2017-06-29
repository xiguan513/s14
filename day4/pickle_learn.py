#!/usr/bin/env python
#-*- coding:utf-8 -*-


import cPickle as pickle

a=["aa","bb",33,11,"2017-05-14:17:10","!wer234@^%$%$sdf"]

# with open("a.pkl","w") as f:
#     pickle.dump(a,f,True)

with open("a.pkl",'r') as f:
    b=pickle.load(f)
    print b
