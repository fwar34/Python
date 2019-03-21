#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: file_content_replace.py
# Author: Feng
# Created Time: Fri 24 Mar 2017 04:27:08 PM CST
# Content: 

import sys
import re

fs = sys.argv[1];
old = sys.argv[2];
new = sys.argv[3];

print('process file {0} content \'{old}\' to new \'{new}\'' . format(fs, old = old, new = new))

file1 = open(fs, 'r+')

line = file1.readline()
print(line, len(line))

print(file1.read(1))

line1 = re.sub('tmServer', 'tmServer1', line)
print(line1, len(line1))

#file1.seek(0, 0)
#file1.write(line1)

content = file1.read();
print(len(content))

content1 = re.sub('tmServer', 'tmServer1', content)
print(len(content1))
print(content1)

file1.write(content1)
file1.close()
