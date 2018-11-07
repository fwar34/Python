#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_fileinput1.py
# Author: Feng
# Created Time: Tue 06 Nov 2018 04:57:53 PM CST
# Content: http://www.jqhtml.com/12874.html
#          http://www.jqhtml.com/12887.html
import fileinput, subprocess, shutil

print('Test fileinput')
with fileinput.input() as f_input:
    for i in f_input:
        print(i)

with fileinput.input('/etc/passwd') as f:
    for line in f:
        print(f.filename(), f.lineno(), line, end = '')
print('end Test fileinput')

print('Test subprocess')
try:
    out_bytes = subprocess.check_output(['netstat', '-a'], timeout = 3)
except subprocess.TimeoutExpired as e:
    print("Exception occur : %s" % e)
else:
    out_text = out_bytes.decode('utf-8')
    print(out_text)

try:
    out_bytes1 = subprocess.check_output('cat /etc/passwd | grep feng', shell = True, timeout = 3)
except subprocess.CalledProcessError as e: 
    print("Call command error : %s" % e)
except subprocess.TimeoutExpired as e:
    print("Exception occur : %s" % e)
else:
    out_text1 = out_bytes1.decode('utf-8')
    print(out_text1)
print('end Test subprocess')


print('Test shutil')
shutil.copy('./test_fileinput1.py', '/tmp')
# Copy files, but preserve metadata (cp -p src dst) -->shutil.copy2(src, dst)
# Copy directory tree (cp -R src dst) -->shutil.copytree(src, dst)
# Move src to dst (mv src dst) -->shutil.move(src, dst)
print('end Test shutil')

# echo $? -->1
raise SystemExit(1)

