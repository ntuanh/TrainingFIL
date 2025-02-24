import socket
import threading

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 8081

# Khởi tạo socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

print("Init Successfully!")

running = True

# check connection
def is_client_connected(client):
    try:
        client.send(b'\x00')  # Gửi một byte rỗng
        return True
    except:
        return False


# def listen_server():
#     global running


def end_program():
    global running
    print("Closing Client socket...")
    running = False
    client_socket.close()

def recv_message():
    global running
    while running:
        try:
            if client_socket.fileno() == -1:  # Check socket are running
                break

            response = client_socket.recv(1024).decode()

            print(f"\nResponse from server: {response}")

            if response == "exit":
                print("Server closed !")
                end_program()

        except OSError:
            print("Server closed!")
            break


def send_message():
    global running
    while running:
        try:
            # Ensure that server are running
            message = input("Enter message or exit: ")

            if message.lower() == "exit":
                end_program()
                break

            # Check socket before send message
            if client_socket.fileno() == -1:
                print("Not connecting to server ! ")
                break

            client_socket.sendall(message.encode())


        except OSError:
            print("Server closed !")
            break

def main():
    global running

    # Init thread and start
    send_thread = threading.Thread(target=send_message)
    recv_thread = threading.Thread(target=recv_message)
    send_thread.start()
    recv_thread.start()

    # End thread
    send_thread.join()
    recv_thread.join()



    print("End Programming")

if __name__ == "__main__":
    main()


