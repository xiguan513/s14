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


#统计
data=Session.query(create_table.User).filter_by(name="Test").count()#统计==select COUNT(*) from `user` where name="Test"
data1=Session.query(create_table.User).filter(create_table.User.name.in_(['Test','li'])).count()#select COUNT(*) from `user` where name="Test" or name="li"

print(data)
print("+++++++++++")
print(data1)


#分组 需要导入单独的模块

from sqlalchemy import func

print(Session.query(func.count(create_table.User.name),create_table.User.name).group_by(create_table.User.name).all())
#==SELECT count(user.name) AS count_1, user.name AS user_name  FROM user GROUP BY user.name

