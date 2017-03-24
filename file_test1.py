#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: file_test1.py
# Author: Feng
# Created Time: Fri 24 Mar 2017 02:27:39 PM CST
# Content: 使用pickle模块将数据对象保存到文件

import pickle

f = open('./workfile', 'wb+')
f.write(b'0123456789')
f.seek(5)
f.read(1)
f.seek(-3, 2)
f.read(1)

data1 = {
        'a' : [1, 2.0, 3, 4 + 6j],
        'b' : ('string', u'Unicode string'),
        'c' : None
        }

list1 = [1, 2, 3]
list1.append(list1)

output = open('./data', 'wb')
#Pickle dictionary using protocol 0
pickle.dump(data1, output)
#Pickle the list using the highest protocol available
pickle.dump(list1, output, -1)

output.close()

#使用pickle模块从文件中重构python对象
import pprint

pklfile = open('./data', 'rb')
data1 = pickle.load(pklfile)
pprint.pprint(data1)

data2 = pickle.load(pklfile)
pprint.pprint(data2)

pklfile.close()
