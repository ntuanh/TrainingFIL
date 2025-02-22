import socket

Server_IP = socket.gethostbyname(socket.gethostname())
Server_PORT = 8081

# Init socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((Server_IP, Server_PORT))
server_socket.listen(1)  # Single-multithreading
print("Server are listening ...")

# connect
client_socket, client_IP = server_socket.accept()
print(f"[+] Message from {client_IP}")

# handle
while True:
    message = client_socket.recv(1024).decode()
    print(f"Content : {message}")
    # Confirm
    client_socket.sendall(f"Server received content :{message}".encode())

    if message.lower() == 'exit':
        break


client_socket.close()
server_socket.close()

