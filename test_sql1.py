#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_sql1.py
# Author: Feng
# Created Time: Tue 30 Oct 2018 04:55:09 PM CST
# Content: 
import sqlite3, os

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print(cursor.rowcount)
conn.commit()

#如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数
#cursor.execute('select * from user where id = ? and pwd = ?', ('abc', 'passwd'))
cursor.execute('select * from user where id = ?', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

os.remove('./test.db')
