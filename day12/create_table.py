#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy import ForeignKey #外键关联


engine=create_engine("mysql+pymysql://root:123456@localhost/testdb?charset=utf8",echo=True) #创建数据库连接 ?charset=utf8 设置字符集
#engine=create_engine("mysql+pymysql://root:123456@localhost/testdb?charset=utf8",echo=True) #创建数据库连接,echo输出打印执行过程


Base=declarative_base()#生成父类

#创建表User
class User(Base):
    __tablename__="user"#指定表名，如果不指定默认使用类名作为表名
    id=Column(Integer,primary_key=True)#创建字段id int 类型并设置为主键，默认自增长
    name=Column(String(32))#创建字段name varchar 类型并指定长度
    password=Column(String(64))

    def __repr__(self): #创建格式字符串，通过orm查询直接返回信息而不是返回一个内存对象信息
        return "id:%s name:%s" % (self.id,self.name)

'''
CREATE TABLE user (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	name VARCHAR(32), 
	password VARCHAR(64), 
	PRIMARY KEY (id)
)

'''



class Status(Base):
    __tablename__="status"
    id=Column(Integer,primary_key=True)
    name=Column(String(32))
    classes=Column(String(32))
    use_id=Column(Integer,ForeignKey("user.id")) #创建外键关联

    def __repr__(self):
        return "id: %s name:%s" %(self.id,self.name)

'''
CREATE TABLE status (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	name VARCHAR(32), 
	classes VARCHAR(32), 
	use_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(use_id) REFERENCES user (id)
)

'''


Base.metadata.create_all(engine)#创建表结构，把所有继承Base类的类都创建为表结构
