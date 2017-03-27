#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: save_file.py
# Author: Feng
# Created Time: 2017年03月27日 星期一 22时37分55秒
# Content: 

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# 获取文件名
fileitem = form['filename']

# 检测文件是否上传
if fileitem.filename:
       # 设置文件路径 
          fn = os.path.basename(fileitem.filename)
          open('/tmp/' + fn, 'wb').write(fileitem.file.read())
             
          message = 'file"' + fn + '"upload success'
                   
else:
          message = 'file not upload'
                      
print ("""\
     Content-Type: text/html\n
                              <html>
                              <head>
                              <meta charset="utf-8">
                              <title>W3C</title>
                              </head>
                              <body>
                                 <p>%s</p>
                                 </body>
                                 </html>
                                 """ % (message,))
