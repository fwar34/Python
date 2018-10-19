#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: robot_client.py
# Author: Feng
# Created Time: Fri 19 Oct 2018 07:58:39 PM CST
# Content: 
import socket
sock = socket.socket()
sock.connect(("localhost", 9999))
sock.settimeout(5)

while True:
    buf = sock.recv(1024)
    print(buf)
    inp = input("输入:").strip()
    sock.send(bytes(inp, encoding = "utf-8"))
    if inp == "exit":
        break

sock.close()
