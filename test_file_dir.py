#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_file_dir.py
# Author: Feng
# Created Time: Mon 29 Oct 2018 04:36:32 PM CST
# Content: 
import os

print(os.name)
print(os.uname())

#环境变量
print(os.environ)
print(os.environ.get('PATH'))

#当前目录
print(os.path.abspath('.'))
#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
testdir = os.path.join('.', 'testdir')
print(testdir)
os.mkdir(testdir)
os.rmdir(testdir)
#同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
#这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
(path, name) = os.path.split('/etc/passwd')
print(path, name)
out = os.path.split('/etc/passwd')
print(out)
#os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便
#这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
out1 = os.path.splitext('/etc/passwd.OLD')
print(out1)

#最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
print([x for x in os.listdir('.') if os.path.isdir(x)])
#要列出所有的.py文件，也只需一行代码
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

