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

#强制指定关联
ret=Session.query(create_table.User,create_table.Status).filter(create_table.User.id==create_table.Status.id).all()
'''
SELECT
	USER .id AS user_id,
	USER . NAME AS user_name,
	USER . PASSWORD AS user_password,
	STATUS .id AS status_id,
	STATUS . NAME AS status_name,
	STATUS .classes AS status_classes
FROM
	USER,
	STATUS
WHERE
	USER .id = STATUS .id
'''

print(ret)


print("==================")
#这种方式必须有外键关联才可以使用
ret1=Session.query(create_table.User).join(create_table.Status,isouter=True).all()

"""
SELECT
	USER .id AS user_id,
	USER . NAME AS user_name,
	USER . PASSWORD AS user_password,
	STATUS .id AS status_id,
	STATUS . NAME AS status_name,
	STATUS .classes AS status_classes,
	STATUS .use_id AS status_use_id
FROM
	USER,
	STATUS
WHERE
	USER .id = STATUS .id;

"""


ret2=Session.query(create_table.User).join(create_table.Status).all()
"""
SELECT
	USER .id AS user_id,
	USER . NAME AS user_name,
	USER . PASSWORD AS user_password
FROM
	USER
INNER JOIN STATUS ON USER .id = STATUS .use_id
"""


print(ret1)



print("=================")

print(ret2)
