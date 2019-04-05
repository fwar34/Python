#-*- coding: utf-8 -*-

# File Name: db.py
# Author: Feng
# Created Time: Fri Apr  5 20:25:02 2019
# Content: execute database operation

import pymysql

conn = pymysql.connect("fwar34.f3322.net", "feng", "1111", "test")
cursor = conn.cursor()

def add_user(name, age, password):
    sql = 'insert into user (name,age,password) values ("{}","{}","{}")' . format(name, age, password)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        print("insert failed")

cursor.close()
conn.close()

if __name__ == '__main__':
    add_user("kai", 32, "111111")
