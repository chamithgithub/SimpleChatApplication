import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",4226))

print("success")