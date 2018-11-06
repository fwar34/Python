#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_thread5-server.py
# Author: Feng
# Created Time: Mon 05 Nov 2018 04:49:53 PM CST
# Content: 
import threading, socket, os, signal

def sig_handler(signum, frame):
    global files
    for f in files:
        os.remove(f)
    print('Catch signal %s, delete test files' % signum)
    exit(0)

signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)
signal.signal(signal.SIGHUP, sig_handler)

files = []
def thread_fun(conn):
    conn.sendall(b'get ready')
    data = conn.recv(1024)
    file_len = int(str(data, encoding = 'utf-8'))

    file_name = 'test.data.%s' % threading.current_thread().ident
    f = open(file_name, 'wb+')
    recv_len = 0
    while True:
        if recv_len == file_len:
            break
        buff = conn.recv(1024)
        f.write(buff)
        recv_len += len(buff)
    f.close()
    conn.close()
    files.append(file_name)
    print('thread %s exit' % threading.current_thread().ident)

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost', 9999))
sock.listen(5)

thds = []
while True:
    conn, addr = sock.accept()
    thd = threading.Thread(target = thread_fun, args = (conn,))
    thd.start()
    thds.append(thd)
sock.close()

for thd in thds:
    thd.join()

for f in files:
    os.remove(f)
print('Server end')
