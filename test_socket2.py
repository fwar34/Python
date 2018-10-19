#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_socket2.py
# Author: Feng
# Created Time: Fri 19 Oct 2018 07:25:30 PM CST
# Content: 

import socket

def handle_request(client):
    buff = client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n", encoding = "utf-8"))
    client.send(bytes("Hello World", encoding = "utf-8"))

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", 9999))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        handle_request(conn)
        conn.close()

if __name__ == "__main__":
    main()
