#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_thread4.py
# Author: Feng
# Created Time: Wed 24 Oct 2018 05:09:26 PM CST
# Content: 全局变量local就是一个ThreadLocal对象 
#ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，
#用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源
import os, threading

local = threading.local()

def process_student():
    std = local.student
    print("Hello %s (in %s)" % (std, threading.current_thread().name))

def process_thread(name):
    local.student = name
    process_student()

ta = threading.Thread(target = process_thread, args = ('Alice',), name = 'Thread-A')
tb = threading.Thread(target = process_thread, args = ('Bob',), name = 'Thread-B')
ta.start()
tb.start()
ta.join()
tb.join()

