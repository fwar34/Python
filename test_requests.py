#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_requests.py
# Author: Feng
# Created Time: 2018/6/2 17:45:57
# Content: 

import requests

def getImageList():
    html = requests.get("http://www.doutula.com/photo/list/?page=2").text
    print(html)

getImageList()
