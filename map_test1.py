#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: map_test1.py
# Author: Feng
# Created Time: Fri 24 Mar 2017 11:03:03 AM CST
# Content: 

map1 = {1:11, '2':22, "3":"33"}
print(map1)

map2 = dict([(1, 11), ('2', 22), ("3", "33")])
print(map2)

map3 = dict(test=33, sss=3234)
print(map3)

map4 = {x:x**2 for x in (2,4,6)}
print(map4)

#在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
for x, y in map1.items():
    print(x, y)

#在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(['tic', "ss", 90]):
    print(i, v)
