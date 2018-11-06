#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_thread5-server2.py
# Author: Feng
# Created Time: Tue 06 Nov 2018 12:37:32 PM CST
# Content: https://www.cnblogs.com/bigberg/p/8044581.html
import socket, select, queue, signal

def sig_handler(signum, frame):
    global is_sigint_recv
    is_sigint_recv = True
    print('Catch signal %s' % signum)
    exit(0)

signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)
signal.signal(signal.SIGHUP, sig_handler)
is_sigint_recv = False

sock = socket.socket()
sock.setblocking(False)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost', 9999))
sock.listen(5)

inputs = [sock]
outputs = []
conn_queue = {}
while True:
    r_list, w_list, e_list = select.select(inputs, outputs, inputs)
    print('select.select')
    # can read
    for s in r_list:
        if s == sock:
            conn, addr = s.accept()
            print("Recv new client %s from %s" % (conn, addr))
            conn.setblocking(False)
            inputs.append(conn)
            conn_queue[conn] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print('Recv data from client %s' % s)
                conn_queue[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                del conn_queue[s]
                print('Close client %s from %s' % (s, s.getpeername()[0]))
                s.close()

    # can write
    for s in w_list:
        # if not conn_queue[s].empty():
            # msg = conn_queue[s].get_nowait()
            # s.send(msg)
            # print('Send to client %s' % s)
        # else:
            # outputs.remove(s)
            # print('Remove client %s write event' % s)
        try:
            msg = conn_queue[s].get_nowait()
        except queue.Empty:
            outputs.remove(s)
            print('Remove client %s write event' % s)
        else:
            s.send(msg)
            print('Send to client %s' % s)

    # error
    for s in e_list:
        print('Client %s socket error' % s)
        if s in outputs:
            outputs.remove(s)
        inputs.remove(s)
        del conn_queue[s]
        s.close()

sock.close()
print('Server end')
