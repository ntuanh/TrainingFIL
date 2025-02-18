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

## Resources :
* [Socket tutorial JS ](https://socket.io/docs/v4/tutorial/introduction)