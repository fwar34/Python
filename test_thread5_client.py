#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_thread5_client.py
# Author: Feng
# Created Time: Mon 05 Nov 2018 04:59:27 PM CST
# Content: 
import socket, os

sock = socket.socket()
sock.connect(('localhost', 9999))
buff = sock.recv(1024)
file_name = 'test_thread5-server.py'
if str(buff, encoding = 'utf-8') == 'get ready':
    file_len = os.stat(file_name).st_size
    sock.sendall(bytes(str(file_len), encoding = 'utf-8'))
    with open(file_name, 'rb') as f:
        for line in f:
            sock.send(line)
