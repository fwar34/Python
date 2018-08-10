#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: raget2.py
# Author: Feng
# Created Time: Tue Aug  7 16:47:52 2018
# Content: 

import os

def getTemp():
    return os.popen('vcgencmd measure_temp').read()[5:9]

def getRam():
    return os.popen('free | tail -n +2').readline()

def getDisk():
    return os.popen('df -h / | tail -n +2').readline()

def getCpuUse():
    return os.popen('top -n1 | awk \'/Cpus/{print $0}\'').readline()

def getCpuUse2():
    return os.popen('top -n1 | tail -n +3').readline()

cpu_temp = getTemp()


