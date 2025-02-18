import socket 

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 8081

# Init socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP , SERVER_PORT))  # Listening on localhost, port 12345
server_socket.listen(1)

print("Server are listening ...")

# Accept connection from client 
conn, addr = server_socket.accept()
print(f"Connection from {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == 'exit':  # If message is "exit" , exit 
        break
    print(f"Client: {data}")
    conn.sendall(f"Server receive : {data}".encode())

conn.close()
server_socket.close()
