import socket
import subprocess

ip = "localhost"
port = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Created socket")
s.connect((ip, port))
print("Connected on " + ip + ":" + str(port))

while True:
    data = s.recv(4)
    if data:
        print("Unlock received, lovely stuff")
    else:
        print("Something went wrong, maybe the connection broke? Shutting down.")
        break
        
