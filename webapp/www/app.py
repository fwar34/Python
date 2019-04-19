#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: app.py
# Author: Feng
# Created Time: 2019-04-17 17:52
# Content:
import logging; logging.basicConfig(level = logging.INFO)

import asyncio
import os
import json
import time

from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body = b'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop = loop)
    app.router.add_route('GET', '/', index)
    server = yield from loop.create_server(app.make_handler(), '0.0.0.0', 5000)
    logging.info('server start at http://%s:%d' % ('0.0.0.0', 5000))
    return server

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
