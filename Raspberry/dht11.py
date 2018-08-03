#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: dht11.py
# Author: Feng
# Created Time: Fri Aug  3 21:45:48 2018
# Content: 
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
gpio = 17

# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
if humidity is not None and temperature is not None:
    print("Temp : {0:0.1f}*C Humidity : {1:0.1f}%".format(temperature, humidity))
else:
    print("Failed to get reading. Try again!")
