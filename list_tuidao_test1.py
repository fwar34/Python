#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: list_tuidao_test1.py
# Author: Feng
# Created Time: Fri 24 Mar 2017 09:59:57 AM CST
# Content: 列表的推导式

v1 = [1, 3, 5]
v2 = [2, 4, 6]
print(v1)
print(v2)

v3 = [x * y for x in v1 for y in v2]
print(v3)

v4 = [v1[i] * v2[i] for i in range(len(v1))]
print(v4)
