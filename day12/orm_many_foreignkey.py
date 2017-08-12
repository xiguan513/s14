#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
多外键关联创建

"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

Base=declarative_base()

class Customer(Base):
    __tablename__='customer'
    id=Column(Integer,primary_key=True)
    name=Column(String(64))

    billing_address_id=Column(Integer,ForeignKey("address.id"))
    shipping_address_id=Column(Integer,ForeignKey("address.id"))

    billing_address=relationship("Address",foreign_keys=[billing_address_id])
    shipping_address=relationship("Address",foreign_keys=[shipping_address_id])
    def __str__(self):
        return self.name

"""
关联多外键
CREATE TABLE customer (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	name VARCHAR(64), 
	billing_address_id INTEGER, 
	shipping_address_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(billing_address_id) REFERENCES address (id), 
	FOREIGN KEY(shipping_address_id) REFERENCES address (id)
)

"""


class Address(Base):
    __tablename__="address"
    id=Column(Integer,primary_key=True)
    street=Column(String(64))
    city=Column(String(64))
    state=Column(String(64))

    def __str__(self):
        return self.street

"""
CREATE TABLE address (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	street VARCHAR(64), 
	city VARCHAR(64), 
	state VARCHAR(64), 
	PRIMARY KEY (id)
)
"""


engine=create_engine("mysql+pymysql://root:123456@localhost/testdb")
#engine=create_engine("mysql+pymysql://root:123456@localhost/testdb",echo=True)

#Base.metadata.create_all(engine)

