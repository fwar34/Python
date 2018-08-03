#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: temp.py
# Author: Feng
# Created Time: Fri Aug  3 12:13:57 2018
# Content: 

file = open("/sys/class/thermal/thermal_zone0/temp")
temp = float(file.read()) / 1000
print("temp : %.3f" % temp)
