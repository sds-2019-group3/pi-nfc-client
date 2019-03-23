# A simple Python client to communicate over ADB with the phone NFC app
# Author: James Atkin

import socket
import subprocess
import time

ip = "localhost"
port = 1337

# Shell command for port forwarding. This allows us to communicate over ADB
command = "sudo adb forward tcp:1337 tcp:1337"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

# Make socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Created socket")
# Connect to server on other end
s.connect((ip, port))
print("Connected on " + ip + ":" + str(port))

# Loop
while True:
    # Get the length of the room name so we know how many bytes to expect
    string_length = int(s.recv(4))
    # Get the room name
    room = s.recv(string_length)
    if room:
        # Download files or whatever in here, go mental
        print("Unlock received for room '" + room + "', lovely stuff")
    else:
        # In this case, we have received some null data. Only bad things can cause this such as unplugging the USB cable, or quitting the server phone-side
        print("Something went wrong, maybe the connection broke? Shutting down.")
        break
