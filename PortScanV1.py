import socket
import sys

target = input("Enter the IP address to scan: ")
targetIP = socket.gethostbyname(target)

# Get the range of ports to scan
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

print ("Starting scan on host", targetIP)

# scan reserved ports 1-65535
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((targetIP, port))
    if result == 0:
        print ("Port {}: Open".format(port))
    else:
        print ("Port {}: Closed".format(port))
    sock.close()

print ("Scanning completed")
