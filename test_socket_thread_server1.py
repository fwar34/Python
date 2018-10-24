#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_socket_thread_server1.py
# Author: Feng
# Created Time: Wed 24 Oct 2018 10:20:42 AM CST
# Content: 
import socket, threading

listensock = socket.socket()
listensock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listensock.bind(("localhost", 9999))
listensock.listen(10)

threads = []

def fun(sock):
    buf = sock.recv(1024)
    print(str(buf, encoding = "utf-8"))
    sock.send(b"Hello")
    sock.close()

while True:
    sock, addr = listensock.accept()
    t = threading.Thread(target = fun, args = (sock,))
    t.start()
    threads.append(t)
listensock.close()

for i in threads:
    i.join()

print("end")
