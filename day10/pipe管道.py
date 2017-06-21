#!/usr/bin/env python
#-*- coding:utf-8 -*-


from multiprocessing import Pipe,Process

def run(conn):
    conn.send("run child")
    data=conn.recv()
    print "in：",data
    conn.close()

if __name__=="__main__":
    parent_conn,child_conn=Pipe()
    p=Process(target=run,args=(child_conn,))
    p.start()
    data=parent_conn.recv()
    print "out:",data
    parent_conn.send("parent con")