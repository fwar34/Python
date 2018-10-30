#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_file2.py
# Author: Feng
# Created Time: Mon 29 Oct 2018 04:11:00 PM CST
# Content: 

path = '/etc/passwd'

try:
    file = open(path, 'r')
    content = file.read()
    print(content)
except IOError as e:
    print(e)
finally:
    if file:
        file.close()

#但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法
#这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法
with open(path, 'r') as f:
    print(f.read())
    data = f.readlines()
    for i in data:
        print(i.strip())

#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
with open('test.py', 'r', encoding = 'gbk') as f1:
    f1.read()

#你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，
#操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
#只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的
#后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：
with open('~/test2222', 'w+') as f2:
    f2.write('Hello world!')


