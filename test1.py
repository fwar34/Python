#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# File Name: test1.py
# Author: Feng
# Created Time: Mon May  7 09:45:30 2018
# Content: https://www.w3cschool.cn/python/python-exercise-example1.html

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (j != k) and (k != i):
                print(i, j, k)
