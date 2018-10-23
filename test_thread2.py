#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_thread2.py
# Author: Feng
# Created Time: Tue 23 Oct 2018 06:00:07 PM CST
# Content: 来看看多个线程同时操作一个变量怎么把内容给改乱了

import threading, time

balance = 0
def change(n):
    global balance
    balance = balance + n
    balance = balance - n

def run(n):
    for i in range(100000):
        change(n)

t1 = threading.Thread(target = run, args = (5,))
t2 = threading.Thread(target = run, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
