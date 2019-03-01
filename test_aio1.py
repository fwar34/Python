#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_aio1.py
# Author: Feng
# Created Time: 2019-03-01 20:05
# Content: 

import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(1)
    print("Hello again!")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
