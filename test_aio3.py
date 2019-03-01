#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_aio3.py
# Author: Feng
# Created Time: 2019-03-01 20:18
# Content: 
import asyncio

@asyncio.coroutine
def wget(host):
    print("gwet %s..." % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'Get / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.baidu.com', 'www.163.com', 'www.bing.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
