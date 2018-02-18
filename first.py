#!/usr/bin/python3
# -*- coding: utf-8 -*-
print('Hello 你好')

s1 = 72
s2 = 85

r = (85 - 72) / 72 * 100
print('%.1f%%' % r)

r = (s2-s1)/s1*100 
print('成绩提升了：%.1f%%' % r)

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

print(L)

print(L[0:3])

str = 'abcdef'
print(str[:3])
print(str[::2])
print(str[2:-2])
for ele in str:
    print(ele)

from collections import Iterable
print(isinstance('abc', Iterable))

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

L = [x * x for x in range(1, 11)]
print(L)

L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

L = [m + n for m in 'abc' for n in 'xyz']
print(L)

import os
L = [d for d in os.listdir('.')]
print(L)

d = {'x' : 'a', 'y' : 'b', 'z' : 'c'}
for k, v in d.items():
    print(k, '=', v)
