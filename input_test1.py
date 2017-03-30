#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: input_test1.py
# Author: Feng
# Created Time: Thu 30 Mar 2017 08:21:56 PM CST
# Content: input函数返回的是str（即unicode编码字符串）,要用int函数转成整数

birth = input('age : ')

if int(birth) > 2000:
    print('00后')
else:
    print('other')
