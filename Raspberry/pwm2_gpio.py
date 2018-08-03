#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: pwm2_gpio.py
# Author: Feng
# Created Time: Fri Aug  3 21:13:35 2018
# Content: 
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

p = GPIO.PWM(40, 50)
p.start(0)

try:
    while True:
        for dc in range(0, 101, 1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        for dc in range(100, -1, -1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
