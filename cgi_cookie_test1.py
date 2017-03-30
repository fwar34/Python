#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: cgi_cookie_test1.py
# Author: Feng
# Created Time: Mon 27 Mar 2017 08:21:18 PM CST
# Content: 测试cookie的设置，给浏览器返回

print('Content-type:text/html')
print('Set-Cookie:name="www.3c";expires=Wed, 28 Aug 2016 18:30:00 GMT')
print()
print("""
    <html>
      <head>
          <meta charset="utf-8">
          <title>cookie test</title>
      </head>
      <body>
          <h1>Cookie set OK!</h1>
      </body>
    </html>
""")
