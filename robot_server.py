#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: robot_server.py
# Author: Feng
# Created Time: Fri 19 Oct 2018 07:52:30 PM CST
# Content: 
import socket

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("localhost", 9999))
sock.listen(5)

while True:
    (conn, addr) = sock.accept()
    conn.sendall(bytes("Hello", encoding = "utf-8"))
    flag = True
    while flag:
        data = conn.recv(1024)
        if data == bytes("exit", encoding = "utf-8"):
            flag = False
        elif data == b"0":
            conn.sendall(bytes("通过可能会被录音.balabala一大堆", encoding = "utf-8"))
        else:
            conn.sendall(bytes("请重新输入.", encoding = "utf-8"))
    conn.close()
