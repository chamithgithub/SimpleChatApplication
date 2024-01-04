import socket

server =socket.socket(socket.AF_INET.SOCK_STREAM)
server.bind(("localhost",4226))
server.listen()

print("wait for client")
client,address=server.accept()
print(f"Client Address {address}")
