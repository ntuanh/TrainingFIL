import socket
import threading
import sys

# get IP and port
SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 8081

# init socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)

print(f"Server is running on {SERVER_IP}:{SERVER_PORT}")

# list clients
clients = []
running = True


# handle client function
def handle_client(client_socket, client_ip):
    print(f"[+] New connection from {client_ip}")
    clients.append(client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message or message.lower() == "exit":
                break
            print(f"[{client_ip}] {message}")
            client_socket.sendall(f"Server received: {message}".encode())
        except:
            break

    print(f"[-] Connection closed from {client_ip}")
    client_socket.close()
    clients.remove(client_socket)


# stop serve function
def stop_server():
    global running
    while True:
        command = input()
        if command.lower() == "exit":
            print("Stopping server...")
            running = False
            server_socket.close()
            print("Server closed")
            for client in clients:
                client.sendall("exit".encode())
                client.close()
            print("Clients closed")
            sys.exit(0)


# Thread stop server
stop_thread = threading.Thread(target=stop_server)
stop_thread.start()

# thread listen from clients
while running:
    try:
        client_socket, client_ip = server_socket.accept()
        if not running :
            break
        print("Start client thread ")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_ip))
        client_thread.start()
    except OSError:
        break

print("Server stopped.")
