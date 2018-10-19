#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_socket_client.py
# Author: Feng
# Created Time: Fri 19 Oct 2018 02:49:32 PM CST
# Content: 
import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 9999))
sk.sendall(bytes("I'm client", encoding = "utf-8"))

ret = str(sk.recv(1024), encoding="utf-8")
print(ret)
