#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_gpio.py
# Author: Feng
# Created Time: Thu Aug  2 22:41:30 2018
# Content: 

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO_PIN = 40

GPIO.setup(GPIO_PIN, GPIO.OUT)

while True:
    GPIO.output(GPIO_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GPIO_PIN, GPIO.LOW)
    time.sleep(0.5)
