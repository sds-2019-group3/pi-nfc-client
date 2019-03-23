import socket
import subprocess
import time

ip = "localhost"
port = 1337

# Shell command for port forwarding. This allows us communicate over ADB
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
    # Receive 4 bytes of data over the socket
    # The only thing ever sent through is "true" when we can unlock the door
    # "true" = 4 chars, hence 4 bytes
    data = s.recv(4)
    # If we get some data, we can know the door we're allowed to enter the room
    if data:
        # Download files or whatever in here, go mental
        print("Unlock received, lovely stuff")
    else:
        # In this case, we have received some null data. Only bad things can cause this such as unplugging the USB cable, or quitting the server phone-side
        print("Something went wrong, maybe the connection broke? Shutting down.")
        break
