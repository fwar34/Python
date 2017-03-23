#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: prime_number1.py
# Created Time: Thu 23 Mar 2017 06:57:37 PM CST
# Author: Feng
# Content: 查找2到10之间的素数（质数） 

for n in range(2, 10):
    #2 in range(2, 2)返回False,所以直接跳到else,range是左闭右开[)
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x) 
            break
    else:
        print(n, 'is a prime number')
