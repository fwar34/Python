#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_socket_udp_B.py
# Author: Feng
# Created Time: Fri 19 Oct 2018 07:42:10 PM CST
# Content: 
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
while True:
    inp = input("数据:").strip()
    if inp == "exit":
        break
    sock.sendto(bytes(inp, encoding = "utf-8"), ("localhost", 9999))

sock.close()
