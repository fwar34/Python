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
