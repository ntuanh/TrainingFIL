import socket

SERVER_IP = socket.gethostbyname(socket.gethostname())

SERVER_PORT = 8081

# init socket
client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client_socket.connect((SERVER_IP , SERVER_PORT))

while True :
    message = input("Enter your message or 'exit' : ")
    client_socket.sendall(message.encode())

    # check exit
    if message.lower() == "exit":
        break

    # confirm that server received message
    response = client_socket.recv(1024).decode()
    print(f"Server received : {response}")

client_socket.close()




