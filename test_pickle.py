#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_pickle.py
# Author: Feng
# Created Time: Mon 29 Oct 2018 05:29:01 PM CST
# Content: 
import pickle
import os

d1 = dict(name = 'Bob', age = 20, score = 89)
print(pickle.dumps(d1))

with open('./obj.data', 'wb+') as f1:
    pickle.dump(d1, f1)

with open('./obj.data', 'rb') as f2:
    d2 = pickle.load(f2)
    print(d2)

os.remove('./obj.data')
