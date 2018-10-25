#!/usr/bin/python3
import os, socket

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("localhost", 9999))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    pid = fork()
    if pid != 0:
        buff = conn.recv(1024)
        print(str(buff, encoding = "utf-8"))
        conn.sendall(b'Hello')
        conn.close()
        print("Child end")
sock.close()
print("Parent end")