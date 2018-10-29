#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_exception1.py
# Author: Feng
# Created Time: Mon 29 Oct 2018 10:05:48 AM CST
# Content: 
import logging

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return n / 10

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError')
        raise

bar()
print('END')
