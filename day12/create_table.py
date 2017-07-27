#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String


engine=create_engine("mysql+pymysql://root:123456@localhost/testdb") #创建数据库连接
#engine=create_engine("mysql+pymysql://root:123456@localhost/testdb",echo=True) #创建数据库连接,echo输出打印执行过程


Base=declarative_base()#生成父类

#创建表User
class User(Base):
    __tablename__="user"#指定表名，如果不指定默认使用类名作为表名
    id=Column(Integer,primary_key=True)#创建字段id int 类型并设置为主键，默认自增长
    name=Column(String(32))#创建字段name varchar 类型并指定长度
    password=Column(String(64))

    def __repr__(self): #创建格式字符串，通过orm查询直接返回信息而不是返回一个内存对象信息
        return "id:%s name:%s" % (self.id,self.name)

Base.metadata.create_all(engine)#创建表结构，把所有继承Base类的类都创建为表结构
