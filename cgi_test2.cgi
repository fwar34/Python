#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: cgi_test2.py
# Author: Feng
# Created Time: Mon 27 Mar 2017 01:40:02 PM CST
# Content: 

import os

print ("Content-type: text/html")
print ()
print ("<meta charset=\"utf-8\">")
print ("<b>env</b><br>")
print ("<ul>")
for key in os.environ.keys():
    print ("<li><span style='color:green'>%30s </span> : %s </li>" % (key,os.environ[key]))
print ("</ul>")
