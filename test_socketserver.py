#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_socketserver.py
# Author: Feng
# Created Time: Fri 19 Oct 2018 08:16:04 PM CST
# Content: 
import socketserver

class myserver(socketserver.BaseRequestHandler):
    
    def handle(self):
        conn = self.request
        conn.sendall(bytes("Hello", encoding = "utf-8"))
        flag = True
        while flag:
            data = conn.recv(1024)
            if data == bytes("exit", encoding = "utf-8"):
                flag = False
            elif data == b"0":
                conn.sendall(bytes('通过可能会被录音.balabala一大推', encoding = "utf-8"))
            else:
                conn.sendall(bytes('请重新输入.', encoding = "utf-8"))

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("localhost", 9999), myserver)
    server.serve_forever()
