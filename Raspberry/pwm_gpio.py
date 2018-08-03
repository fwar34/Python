#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: pwm_gpio.py
# Author: Feng
# Created Time: Fri Aug  3 21:06:55 2018
# Content: 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

p = GPIO.PWM(40, 1)
p.start(50)
input("Press any key to stop :")
p.stop()

GPIO.cleanup()
