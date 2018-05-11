#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# File Name: test2.py
# Author: Feng
# Created Time: Tue May  8 19:40:17 2018
# Content: https://www.w3cschool.cn/python/python-exercise-example2.html

total = int(input("Enter a number: "))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

r = 0
for i in range(0, 6):
    if (total > arr[i]):
        r += (total - arr[i]) * rat[i]
        print((total - arr[i]) * rat[i])
        total = arr[i]

print(r)
