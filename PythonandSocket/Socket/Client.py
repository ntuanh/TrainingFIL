import socket

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 8081

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))  # Connect to server

while True:
    msg = input("Enter your message or exit : ")
    client_socket.sendall(msg.encode())

    if msg.lower() == 'exit':
        break

    response = client_socket.recv(1024).decode()
    print(f"Server: {response}")

client_socket.close()
