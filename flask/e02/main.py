#-*- coding: utf-8 -*-

# File Name: main.py<e02>
# Author: Feng
# Created Time: Fri Apr  5 19:08:22 2019
# Content: 

import pymysql

#打开数据库连接
db = pymysql.connect("fwar34.f3322.net", "feng", "1111", "test")

#使用curson创建一个游标
cursor = db.cursor()

#使用execute方法执行sql查询
cursor.execute("select version()")

#使用fetchone方法获取单条数据
data = cursor.fetchone()

print("Database version %s" % data)

cursor.execute("show tables")

#execute返回的结果集是tuple, 里面的每个元素还是tuple
data_all = cursor.fetchall()
print(type(data_all))

user_table_exist = False
for element in data_all:
    if element[0] == 'user':
        print('%s exist' % element)
        user_table_exist = True

sql_create_table = '''
                   create table user(id int auto_increment primary key, name char(10) not 
                   null unique, age tinyint not null) default charset=utf8;
                   '''

if not user_table_exist:
    cursor.execute(sql_create_table)
# if not ('user',) in data_all:
#     cursor.execute(sql_create_table)

sql_insert = '''
insert into user (id,name,age) values (1, 'feng', 31)
'''
try:
    cursor.execute(sql_insert)
    print("insert")
except:
    print("insert failed")
else:
    db.commit()

cursor.execute('select * from user')
users = cursor.fetchall()
for ele in users:
    print(ele)

name = input("enter your name:").strip()
age = input("enter you age:").strip()
sql_insert2 = 'insert into user (name,age) values ("{}","{}")' . format(name, int(age))
cursor.execute(sql_insert2)
db.commit()

#关闭光标对象
cursor.close()
#关闭数据库
db.close()
