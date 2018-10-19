#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_socket_udp.py
# Author: Feng
# Created Time: Fri 19 Oct 2018 07:38:12 PM CST
# Content: 
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.bind(("localhost", 9999))

while True:
    buff = sock.recv(1024)
    print(str(buff, encoding = "utf-8"))
