#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_class2.py
# Author: Feng
# Created Time: 2018/5/22 22:23:53
# Content: 

class Person:
    name = ""
    age = 0
    count = 0
    count2 = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.count += 1
        Person.count2 += 1

    def dump(self):
        print(self.name, self.age, self.count, Person.count2)


son1 = Person("son1", 10)
son1.dump()
son2 = Person("son2", 12)
son2.dump()
