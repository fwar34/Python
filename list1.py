#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: li1.py
# Author: Feng
# Created Time: Fri 13 Apr 2018 08:45:34 PM PDT
# Content: 

li = ["a", "b", "c"]
print(li)

del(li[2])
print(li)

li.append("d")
print(li)

print(len(li))
print(li*4)

print(3 in li)

for x in li:
    print(x)

tu = (1, 2, 3)
li2 = list(tu)
print(li2)

li2.append(3)
print(li2.count(3))

li2.extend(tu)
print(li2)

print(li2.index(2))

num = li2.pop()
print(num)

li2.remove(2)
print(li2)

li2.reverse()
print(li2)

li2.sort()
print(li2)
