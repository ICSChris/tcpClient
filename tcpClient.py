import socket

targetHost = "127.0.0.1"
targetPort = 2600

# Create a socket object and pass to client variable
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the client
client.connect((targetHost,targetPort))

# Transmit data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive data
response = client.recv(4096)

print(response)

