#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_sql3.py
# Author: Feng
# Created Time: Tue 30 Oct 2018 06:12:31 PM CST
# Content: 
import mysql.connector

with mysql.connector.connect(user = 'root', password = '111111', database = 'test') as conn:
    cursor = conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
    print(cursor.rowcount)
    conn.commit()
    cursor.close()
