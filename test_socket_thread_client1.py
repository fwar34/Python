#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_socket_thread_client1.py
# Author: Feng
# Created Time: Wed 24 Oct 2018 10:26:39 AM CST
# Content: 
from multiprocessing import Process
import os, socket

def func():
    sock = socket.socket()
    sock.connect(("localhost", 9999))
    sock.send(b"I'm client")
    buf = sock.recv(1024)
    print(str(buf, encoding = "utf-8"))
    sock.close()

pids = []
if __name__ == '__main__':
    for i in range(100):
        p = Process(target = func)
        p.start()
        pids.append(p)

    for i in pids:
        i.join()

    print("end")
