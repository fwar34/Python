#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

print('hello emacs')

a = 10
if a >= 1:
    print(a)
else:
    print(-a)

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)

def qua(a, b, c):
    det = math.sqrt(b * b - 4 * a *c)
    x = (-b + det) / 2 * a
    y = (-b - det) / 2 * a
    return x, y

print(qua(2, 3, 1))
print(qua(1, 3, -4))
