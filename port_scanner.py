#!/bin/python

import sys
import socket
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip> e.g. 192.168.0.111")

# Add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
    for port in range(int(input("Pick starting port: ")),
    int(input("Pick ending port: "))):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, port)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) # Returns an error indicator
        if result == 0:
            print(f"Port {port} is open.")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved ?__?")
    sys.exit()

except socket.error:
    print("Could not connect to server X__X")
    sys.exit()
