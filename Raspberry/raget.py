#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: raget.py
# Author: Feng
# Created Time: Fri Aug  3 12:18:37 2018
# Content: http://shumeipai.nxez.com/2014/10/04/get-raspberry-the-current-status-and-data.html

import os

def getCPUtemperature():
    res = os.popen("vcgencmd measure_temp").readline()
    return (res.replace("temp=", "").replace("'C\n", ""))

# Return RAM information (unit=kb) in a list                                       
# Index 0: total RAM                                                               
# Index 1: used RAM                                                                 
# Index 2: free RAM 
def getRAMinfo():
    p = os.popen('free')
    i = 0;
    while True:
        line = p.readline()
        i = i + 1
        if (i == 2):
            return line.split()[1:4]

# Return information about disk space as a list (unit included)                     
# Index 0: total disk space                                                         
# Index 1: used disk space                                                         
# Index 2: remaining disk space                                                     
# Index 3: percentage of disk used  
def getDiskSpace():
    res = os.popen("df -h /")
    i = 0
    while True:
        line = res.readline()
        i = i + 1
        if (i == 2):
            return line.split()[1:5]

# cpu温度获取这样写会不会更轻巧些
# def getCPUtemperature():
    # return os.popen( ‘/opt/vc/bin/vcgencmd measure_temp’  ).read()[5:9]
# 或者直接读取系统自己的状态更新，省去模拟shell
# def getCPUtemperature():
    # with open( “/sys/class/thermal/thermal_zone0/temp”  ) as tempFile:
        # res = tempFile.read()
        # res=str(float(res)/1000)
        # return res


# 同理，getRaminfo()可以写成： return os.popen(‘free|tail -n +2’).readline().split()[1:4]
# getDiskSpace()可以写成：return os.popen(‘df -h /|tail -n +2’).readline().split()[1:5]
# popen的效率不高，但是配合shell相当灵活～～


# Return % of CPU used by user as a character string 
def getCPUuse():
    return str(os.popen("top -n1|awk '/Cpu\(s\)/{print $2}'").readline().strip())

CPU_temp = getCPUtemperature()
CPU_usage = getCPUuse()

RAM_status = getRAMinfo()
RAM_total = round(int(RAM_status[0]) / 1000, 1)
RAM_used = round(int(RAM_status[1]) / 1000, 1)
RAM_free = round(int(RAM_status[2]) / 1000, 1)

DISK_status = getDiskSpace()
DISK_total = DISK_status[0]
DISK_used = DISK_status[1]
DISK_free = DISK_status[2]
DISK_perc = DISK_status[3]

if __name__ == '__main__':
    print('')
    print('CPU Temperature = ' + CPU_temp + "'C")
    print('CPU Use = ' + CPU_usage)
    print('')
    print('RAM Total = ' + str(RAM_total) + ' MB')
    print('RAM Used = ' + str(RAM_used) + ' MB')
    print('RAM Free = ' + str(RAM_free) + ' MB')
    print('')  
    print('DISK Total Space = ' + str(DISK_total) + 'B')
    print('DISK Used Space = ' + str(DISK_used) + 'B')
    print('DISK Free Space = ' + str(DISK_free) + 'B')
    print('DISK Used Percentage = ' + str(DISK_perc))
