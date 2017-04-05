#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: function_test3.py
# Author: Feng
# Created Time: Wed 05 Apr 2017 08:32:41 PM CST
# Content: 

def kw_func(name, age = 20, **kw):
    print("name : %s, age : %d\n" % (name, age))
    for n in kw:
        print(n, ":", kw[n])

kw_func("feng", 21, city="Xi'an", code=22222)
