#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
多对多关系
example
    图书与作者关系的表结构
    1 一个本书可以有多个作者一起出版
    2 一个作者可以写多本书
    
    author （作者）
        id  name  email 
        1   song  song@mail.com
        2   bing  bing@mai.com
        3   liapan li@mail.com
    
    book （书名）
        id name         pub_date
        1   学习python   出版日期
        2   学习shell
        3   学习运维
        4   mysql学习
    
    
"""
from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base=declarative_base()

#table 方式创建表 ，orm 自动维护表数据
book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )

"""
CREATE TABLE book_m2m_author (
	book_id INTEGER, 
	author_id INTEGER, 
	FOREIGN KEY(book_id) REFERENCES books (id), 
	FOREIGN KEY(author_id) REFERENCES authors (id)
)
"""



class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref='books')#多对多关系映射

    def __repr__(self):
        return self.name

"""
CREATE TABLE books (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	name VARCHAR(64), 
	pub_date DATE, 
	PRIMARY KEY (id)
)
"""

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name

"""
CREATE TABLE authors (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	name VARCHAR(32), 
	PRIMARY KEY (id)
)
"""

#engine=create_engine("mysql+pymysql://root:123456@localhost/testdb")
engine=create_engine("mysql+pymysql://root:123456@localhost/testdb?charset=utf8",echo=True)

Base.metadata.create_all(engine)