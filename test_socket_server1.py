#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_socket_server.py
# Author: Feng
# Created Time: Fri 19 Oct 2018 02:43:25 PM CST
# Content: 

import socket

sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(("127.0.0.1", 9999))
sk.listen(5)

while True:
    conn, addr = sk.accept()
    client_data = str(conn.recv(1024), encoding = "utf-8")
    print(client_data)
    conn.sendall(bytes("Hello", encoding = "utf-8"))
    conn.close()
