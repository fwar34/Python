#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: dht11_gpio.py
# Author: Feng
# Created Time: Fri Aug  3 21:59:03 2018
# Content: 
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmod(gpio.BOARD)

data = []
def delay(i):
    a = 0
    for j in range(i):
        a + 1

j = 0
gpio.setup(17, gpio.OUT)
