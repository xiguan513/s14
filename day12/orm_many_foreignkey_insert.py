#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
多外键关联创建c插入数据

"""

from s14.day12 import orm_many_foreignkey

from sqlalchemy.orm import sessionmaker

Session_class=sessionmaker(bind=orm_many_foreignkey.engine)
session=Session_class()

#插入数据
# addr1=orm_many_foreignkey.Address(street="liujiayao",city="chaoyang",state="beijing")
# addr2=orm_many_foreignkey.Address(street="sanyuan",city="chaoyang",state="beijing")
# addr3=orm_many_foreignkey.Address(street="fenzhognsi",city="fengtai",state="beijing")
#
# session.add_all([addr1,addr2,addr3])
# c1=orm_many_foreignkey.Customer(name="song",billing_address=addr1,shipping_address=addr2)
# c2=orm_many_foreignkey.Customer(name="tom",billing_address=addr3,shipping_address=addr3)
#
# session.add_all([c1,c2])
# session.commit()

#查询数据
obj=session.query(orm_many_foreignkey.Customer).filter(orm_many_foreignkey.Customer.name=="song").first()
print obj.name,obj.billing_address,obj.shipping_address