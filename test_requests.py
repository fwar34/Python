#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_requests.py
# Author: Feng
# Created Time: 2018/6/2 17:45:57
# Content: 

import requests
import re
import pymysql

# 连接数据库
# db = pymysql.connect(host = '127.0.0.1', port = 3306, 
        # db = 'test', user = 'root', passwd = 'root', charset = 'utf-8')
# 创建游标
# cursor = db.cursor()
# cursor.execute("select * from images")
# print(cursor.fetchall())

def getImageList(page = 1):
    # 获取网页源代码 content
    html = requests.get("http://www.doutula.com/photo/list/?page={}".format(page)).text
    print(html)
    
    # 匹配所有".*?", 加括号的是分组，要返回结果的
    reg = r'data-original="(.*?)".*?alt="(.*?)"'
    # S 多行匹配, compile编译为对象, 增加效率
    reg = re.compile(reg, re.S)
    imageList = re.findall(reg, html)
    for i in imageList:
        print(i)

getImageList(2)
