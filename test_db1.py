#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_db1.py
# Author: Feng
# Created Time: Thu 01 Nov 2018 05:58:40 PM CST
# Content: 
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'name'
    id = Column(String(20), primary_key = True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://root:111111@localhost:3306/test')
DBSession = sessionmaker(bind = engine)

if __name__ == '__main__':
    session = DBSession()
    new_user = User(id = '5', name = 'Bob')
    session.add(new_user)
    session.commit()
    session.close()

