#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: cgi_test3.py
# Author: Feng
# Created Time: Mon 27 Mar 2017 08:04:06 PM CST
# Content: 

import cgi, cgitb

#创建FieldStorage的实例化
form = cgi.FieldStorage()

#获取数据
site_name = form.getvalue('name')
site_url = form.getvalue('url')

print ("Content-type:text/html")
print ()
print ("<html>")
print ("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>xx</title>")
print ("</head>")
print ("<body>")
print ("<h2>%s %s</h2>" % (site_name, site_url))
print ("</body>")
print ("</html>")
