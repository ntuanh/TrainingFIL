import socket
import os

Server_IP = socket.gethostbyname(socket.gethostname())
Server_PORT = 8081


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((Server_IP, Server_PORT))
server_socket.listen(1)

print(f"Server is listening on {Server_IP}:{Server_PORT}...")


client_socket, client_IP = server_socket.accept()
print(f"[+] Connected to {client_IP}")


file_name = client_socket.recv(1024).decode()
print(f"Receiving file: {file_name}")


file_size = int(client_socket.recv(1024).decode())
print(f"File size: {file_size} bytes")


with open(f"received_{file_name}", "wb") as file:
    received_size = 0
    while received_size < file_size:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        file.write(chunk)
        received_size += len(chunk)

print(f"File {file_name} received successfully!")


client_socket.sendall(f"Server received file {file_name}".encode())

client_socket.close()
server_socket.close()
print("Server closed.")
