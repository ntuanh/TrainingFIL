import socket
import threading
import sys

# Get IP and Port
SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 8081

# Init socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)

print(f"Server is running on {SERVER_IP}:{SERVER_PORT}")

# List clients
clients = []
running = True


# Handle client function
def handle_client(client_socket, client_ip):
    """ Xử lý client khi có kết nối """
    print(f"[+] New connection from {client_ip}")
    clients.append(client_socket)

    while running:
        try:
            message = client_socket.recv(1024).decode()
            if not message or message.lower() == "exit":
                break

            print(f"[{client_ip}] {message}")
            client_socket.sendall(f"Server received: {message}".encode())

        except (ConnectionResetError, OSError):
            break  #

    print(f"[-] Connection closed from {client_ip}")
    client_socket.close()
    if client_socket in clients:
        clients.remove(client_socket)  # remove clients


# Stop server function
def stop_server():
    """ Nhập 'exit' trên server để dừng tất cả clients """
    global running
    while running:
        command = input()
        if command.lower() == "exit":
            print("Stopping server...")
            running = False

            for client in clients:
                try:
                    client.sendall("exit".encode())
                    client.close()
                except OSError:
                    pass
            clients.clear()

            server_socket.close()
            print("Server closed")
            sys.exit(0)


stop_thread = threading.Thread(target=stop_server, daemon=True)
stop_thread.start()


while running:
    try:
        client_socket, client_ip = server_socket.accept()
        print("Start client thread")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_ip))
        client_thread.start()
    except OSError:
        break

print("Server stopped.")
