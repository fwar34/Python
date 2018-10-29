#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_exception.py
# Author: Feng
# Created Time: Mon 29 Oct 2018 10:02:42 AM CST
# Content: 
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
