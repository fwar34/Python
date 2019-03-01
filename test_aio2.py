#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_aio2.py
# Author: Feng
# Created Time: 2019-03-01 20:12
# Content: 

import threading
import asyncio

@asyncio.coroutine
def hello():
    print("Hello world! (%s)" % threading.currentThread())
    yield from asyncio.sleep(1)
    print("Hello again! (%s)" % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
