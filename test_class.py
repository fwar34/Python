#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_class.py
# Author: Feng
# Created Time: 2018/5/21 22:17:49
# Content: 

class Person:
    count = 0 #类变量,静态变量

    def __init__(self, name, age):
        self.name = name #self.name和self.age是实例变量
        self.age = age
        Person.count += 1

    def dump(self):
        print(self.name, self.age, Person.count)

liang = Person("liang.feng", 31)
liang.dump()
jing = Person("jing", 30)
jing.dump()
