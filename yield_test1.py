#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: yield_test1.py
# Author: Feng
# Created Time: Thu 23 Mar 2017 08:13:14 PM CST
# Content: yield函数测试

import sys

def fibonacci(n): #生成器函数--斐波那契数列
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)  #f是一个迭代器，由生成器函数返回

while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()
