#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_thread1.py
# Author: Feng
# Created Time: Tue 23 Oct 2018 05:52:03 PM CST
# Content: 
import time, threading

def function():
    print("Thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("Thread %s >>>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("Thread %s end" % threading.current_thread().name)

print("Thread %s is running..." % threading.current_thread().name)
t = threading.Thread(target = function, name = "my function")
t.start()
t.join()
print("Thread %s is end" % threading.current_thread().name)
