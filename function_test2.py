#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: function_test2.py
# Author: Feng
# Created Time: Wed 05 Apr 2017 08:30:01 PM CST
# Content: 

def arg_func(name, age = 18, *arg):
    print("name : %s, age : %d\n" % (name, age))
    for n in arg:
        print(n)

arg_func("feng", 20, "sss")
