import socket
import os
import sys

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 8081

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

file_name = "test.txt"
file_size = os.path.getsize(file_name)

client_socket.sendall(file_name.encode())

client_socket.sendall(str(file_size).encode())

with open(file_name, "rb") as file:
    while chunk := file.read(1024):
        client_socket.sendall(chunk)

print("File sent successfully!")

response = client_socket.recv(1024).decode()
print(f"Server response: {response}")

client_socket.close()
sys.exit(0)
