#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: cgi_cookie_test2.py
# Author: Feng
# Created Time: Mon 27 Mar 2017 08:27:52 PM CST
# Content: 

import os
import Cookie

print('Context-type:text/html')
print()
print("""
    <html>
    <head>
    <meta charset="utf-8">
    <title>W3C</title>
    </head>
    <body>
    <h1>read cookie info</h1>
""")

if 'HTTP_COOKIE' in os.environ:
    cookie_str = os.environ.get('HTTP_COOKIE')
    c = Cookie.SimpleCookie()
    c.load(cookie_str)

    try:
        data = c['name'].value
        print ("cookie data: "+data+"<br>")
    except KeyError:
        print ("cookie is not set<br>")
print ("""
    </body>
    </html>
""")
