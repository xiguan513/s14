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
user_obj1=create_table.User(name="bing",password="123456")
user_obj2=create_table.User(name="li",password="123456")
user_obj3=create_table.User(name="pan",password="123456")

sta_obj=create_table.Status(id=1,name="song",classes="yuwen",use_id=1)
sta_obj1=create_table.Status(id=2,name="song",classes="matsh",use_id=1)
sta_obj2=create_table.Status(id=3,name="bing",classes="yuwen",use_id=2)

Session.add_all([sta_obj,sta_obj1,sta_obj2])

Session.commit()