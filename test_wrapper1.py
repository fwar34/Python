#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_wrapper1.py
# Author: Feng
# Created Time: Wed 07 Nov 2018 07:39:45 PM CST
# Content: http://python.jobbole.com/81683/
# 装饰器测试

def add1(x, y):
    return x + y

def wrapper(func):
    def inner(*args, **kwargs):
        # 这个装饰器判断参数是否小于0，小于0就跑出异常
        for i in args:
            if i < 0:
                raise BaseException
        print("args:%s|kwargs:%s" % (args, kwargs))
        return func(*args, **kwargs)
    return inner

###########################################
# 手动装饰
func1 = wrapper(add1)
print(func1(1, 3))

try:
    print(func1(-1, 3))
except BaseException:
    print("add2 raise BaseException")

###########################################
# @装饰
@wrapper
def add2(x, y):
    return x - y

print(add2(3, 5))

try:
    print(add2(-5, 3))
except BaseException:
    print("add2 raise BaseException")
