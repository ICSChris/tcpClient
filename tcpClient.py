import socket

target_host = "127.0.0.1"
target_port = 2600

# Create a socket object and pass to client variable
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the client
client.connect((target_host,target_port))

# Transmit data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive data
response = client.recv(4096)

print(response)

