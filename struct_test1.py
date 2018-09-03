#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: struct_test1.py
# Author: Feng
# Created Time: Mon 03 Sep 2018 02:34:40 PM CST
# Content: 

import struct

def test():
    return struct.pack('<3I2H2I', 1, 2, 3, 4, 5, 6, 7)

print(test())
