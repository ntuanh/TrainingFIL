## Socket :
* Socket is an endpoint for communication between 2 machines over network .
* Allow programs to send receive data across the internet or local network .

#### Types of Socket :
* Stream Socket ( TCP )  : Reliable , connection-based communication .
* Datagram Socket ( UDP ): Unreliable , fast 

#### How Sockets work : 
* [1]   Create a socket   - A program creates a socket using system call .
* [2]   Binding           - The socket assign to an IP address and port .
* [3]   Listening ( for severs )  - The servers wait for incoming connection .
* [4]   Connection( for clients)  - The clients connect to the server .
* [5]   Data Transmission     - 2 machines exchange messages .
* [6]   Closing the socket .

### Socket families 
* `AF_UNIX`     : is an address family , using domain sockets instead network sockets .
* `AF_INET`     : is an address family , IPv4 
* `AF_INET6`    :
* `AF_CAN`      :

* `SOCK_STREAM` : uses TCP protocol , reliable .
* `SOCK_DGRAM`  : 

### Commands :
* `server_socket.bind(('IP' , PORT)) ` : assigns IP address and port .
* `server_socket.listen(n)` : n is the max number of queued connections ( maximum n clients ).
* `.server_socket.accept()`  : return a socket and a an IP address for each client .
* `.recv(1024)`         : receive 1024 byte per time .
* `.decode() `   : bytes to string .
* `.encode() `   : string to bytes .

* `socket.gethostname()` : get machine's name , return name string .
* `socket.gethostbyname(hostname)` : get IP address of hostname , return IP .

* `sudo netstat -tuln`   : Display all the ports running .
* `sudo netstat -tulpn` : Display all the ports running , with PID .
* `sudo kill -9 13958`   : `13958` is the PID ( Process ID ) not PORT .



## Resources :
* [Socket tutorial JS ](https://socket.io/docs/v4/tutorial/introduction)
* [Socket tutorial Python ](https://docs.python.org/3/library/socket.html)   