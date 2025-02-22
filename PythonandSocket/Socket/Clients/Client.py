import socket
import threading
import sys

SERVER_IP = socket.gethostbyname(socket.gethostname())

SERVER_PORT = 8081

# init socket
client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client_socket.connect((SERVER_IP , SERVER_PORT))

print("Init Successfully ! ")

running = True

def send_message():
    print("Starting Send message function !")
    global running
    message = input("Enter your message or 'exit' in here : ")
    client_socket.sendall(message.encode())

    if message.lower() == "exit":
        client_socket.close()
        running = False
        print("Closed Client socket")

    response = client_socket.recv(1024).decode()
    print(response)

def check_stopping():
    print("Starting Check Stopping function ! ")
    global running
    response = client_socket.recv(1024).decode()
    if response == "exit":
        running = False
        client_socket.close()
        print("Closed Client socket in check stopping function ")

stop_thread = threading.Thread(target= check_stopping)
stop_thread.start()

while running:
    print("In running while loop ")
    try:
        main_thread = threading.Thread(target=send_message)
        main_thread.start()
    except:
        break

print("End Programing")






