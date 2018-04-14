#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: tuple1.py
# Author: Feng
# Created Time: Fri 13 Apr 2018 09:01:34 PM PDT
# Content: 

tu = (1, 2, 3)
print(tu)

tu1 = ()
print(tu1)

tu2 = (1,)
print(tu2)

tu3 = tu + tu2
print(tu3)

del tu3
#print(tu3)

li = [2, 3, 4]
tu4 = tuple(li)
print(tu4)
