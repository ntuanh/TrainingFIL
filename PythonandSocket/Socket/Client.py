# import socket

# SERVER_IP = "192.168.100.100"
# SERVER_PORT = 8081

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect((SERVER_IP, SERVER_PORT))  # Connect to server

# while True:
#     msg = input("Enter your message or exit : ")
#     client_socket.sendall(msg.encode())

#     if msg.lower() == 'exit':
#         break

#     response = client_socket.recv(1024).decode()
#     print(f"Server: {response}")

# client_socket.close()


import socket

def start_client(server_host='192.168.100.100', server_port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_host, server_port))
        print(f"Connected to server at {server_host}:{server_port}")

        message = "Hello, Server!"
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent: {message}")

        data = client_socket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")


start_client() 
