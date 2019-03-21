#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: args.py
# Author: Feng
# Created Time: Thu 11 Oct 2018 02:30:07 PM CST
# Content: 

def sum(*arg):
    total = 0
    for i in arg:
        total += i
    return total

print(sum(1, 2, 3))
print(sum(1, 2))

def mobile(brand, **detail):
    print("Brand : {}, Detail : {}" . format(brand, detail))

mobile("mix2")
mobile("mix2", price = 3000)
mobile("mix2", price = 3000, cpu = 8)

def mobile2(**detail):
    print("detail : {}" . format(detail))

mobile2(price = 1111, cpu = 8)
