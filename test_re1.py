#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_re1.py
# Author: Feng
# Created Time: Tue 30 Oct 2018 03:07:49 PM CST
# Content: 
import re
if re.match(r'\d{3}\-\d{3,8}$', '010-12345'):
    print('OK')
else:
    print('Not match')
if re.match(r'\d{3}\-\d{3,8}$', '010 12345'):
    print('OK')
else:
    print('Not match')

#用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码
print('a b   c'.split(' '))
#嗯，无法识别连续的空格，用正则表达式试试
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a, b,    c d'))

#分组group
m = re.match(r'(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))

#贪婪匹配
m1 = re.match(r'(\d+)(0*)$', '102400')
print(m1.groups())

#非贪婪
m2 = re.match(r'(\d+?)(0*)$', '123400')
print(m2.groups())
