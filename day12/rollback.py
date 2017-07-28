#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from day12 import create_table #导入表信息


engine=create_engine("mysql+pymysql://root:123456@localhost/testdb")


session_class=sessionmaker(bind=engine) #创建与数据库连接回话的类
Session=session_class()#生成实例,游标功能

#data=Session.query(create_table.User).filter_by(name="song")#查询出来的是列表,条件查询
data=Session.query(create_table.User).filter_by(name="Test").all()#查询出来一组对象==select * from `user` where name="song"

print(data)
data[0].name="Test"
data[0].password="11111111111111" #修改数据

data=Session.query(create_table.User).filter_by(name="Test").all()
print(data[0].password)

Session.rollback()#回滚

print("rollbakc after data")
data=Session.query(create_table.User).filter_by(name="Test").all()
print(data[0].password)

Session.commit()