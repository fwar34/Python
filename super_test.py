#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: super_test.py
# Author: Feng
# Created Time: Thu 11 Oct 2018 03:24:10 PM CST
# Content: 

class Base:
    def hello(self):
        print("Base hello")

class Derived(Base):
    def hello(self):
        print("Derived hello")
        super().hello()

d = Derived()
d.hello()

##########################################################
class Base2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Derived2(Base2):
    def __init__(self, name, age, home):
        super().__init__(name, age)
        self.home = home

d2 = Derived2("Leo", 30, "China")
print(d2.name)
