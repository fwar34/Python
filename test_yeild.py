#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_yeild.py
# Author: Feng
# Created Time: 2019-03-01 19:36
# Content: https://blog.csdn.net/hedan2013/article/details/56293173
def mygenerator():
    print("before first yield")
    value = (yield 1)
    # value = yield 1
    print("first yield input, value = %s" % value)
    value = (yield value)
    print("second yield input, value = %s" % value)

# mygenerator()
if __name__ == '__main__':
    gen = mygenerator()
    print("first yield output %s" % next(gen))
    print("second yield output %s" % gen.send(4))
    print(gen.send(7))
