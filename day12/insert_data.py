#!/usr/bin/env python
#-*- coding:utf-8 -*-



import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from day12 import create_table #导入表信息



engine=create_engine("mysql+pymysql://root:123456@localhost/testdb",echo=True)


session_class=sessionmaker(bind=engine) #创建与数据库连接回话的类
Session=session_class()#生成实例,游标功能

user_obj=create_table.User(name="song", password="123456")

print(user_obj)

Session.add(user_obj)

Session.commit()