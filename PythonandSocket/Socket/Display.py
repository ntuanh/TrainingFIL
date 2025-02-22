import socket

def get_local_ip():
    try:
        # Connect to an external server (Google's DNS) but don't send data
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            print(s.getsockname()[0])
    except Exception as e:
        print(f"Error: {e}")


get_local_ip()

# print("Check Ip address ")
# hostname = socket.gethostname()
# print(f"Host name : {hostname}")

# ip_localhost =socket.gethostbyname('localhost')
# print(f"IP local host : {ip_localhost}")

# ip_private = socket.gethostbyname(hostname)
# print(f"IP private : {ip_private}")



