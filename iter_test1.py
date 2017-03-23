#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: iter_test1.py
# Author: Feng
# Created Time: Thu 23 Mar 2017 08:09:50 PM CST
# Content: 测试迭代器 

import sys

list = [1, 2, 3, 4]
it = iter(list)

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
