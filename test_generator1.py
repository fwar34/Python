#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_generator1.py
# Author: Feng
# Created Time: Tue 13 Nov 2018 05:47:12 PM CST
# Content: 
import os
# 列表生成式
l = [ x * x for x in range(10) ]
print(l)
# 生成器
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print("==============")
for n in g:
    print(n)
print('==============')

def fib(max):
    n = 0
    a = 1
    b = 1
    while n < max:
        print(b)
        # a, b = b, a + b相当于
        # t = (b, a + b) t是一个元组
        # a = t[0]
        # b = t[1]
        a, b = b, a + b
        n = n + 1
    return 'done'


#将print(b)改成yield b就成了一个生成器
def fib2(max):
    n = 0
    a = 1
    b = 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for n in fib2(10):
    print(n)

f = fib2(10)
while True:
    try:
        x = next(f)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

d = odd()
next(d)
next(d)
next(d)
try:
    next(d)
except StopIteration as e:
    print('Catch StopIteration')

#杨辉三角
def triangles(max):
    L = [1]
    while len(L) <= max:
        yield L
        L = [1] + [L[x - 1] + L[x] for x in range(1, len(L))] + [1]

ret = []
for n in triangles(10):
    ret.append(n)

print(ret)

