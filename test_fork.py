#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_fork.py
# Author: Feng
# Created Time: Tue 23 Oct 2018 03:07:05 PM CST
# Content: 
import os
print('Process (%s) start' % os.getpid())

pid = os.fork()
if pid == 0:
    print('I am child, pid(%s) ppid(%s)' % (os.getpid(), os.getppid()))
else:
    print('I (%s) create a child (%s)' % (os.getpid(), pid))
    
