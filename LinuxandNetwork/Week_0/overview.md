## 1. Servers and Client  
* A Server is a computer or software that provides services, data, or resources to other devices (aka Client) over a network.  
* A client is a device, software, or system that requests services, data, or resources from a server in a network. It can be a computer, smartphone, or any device that interacts with a server.

![Server and Client model](../Week_0/ServerAndClient_resized.png)

## 2. Forwarding  
* **Forwarding** is the process of sending a message from one node to another node in the network (Destination, Next Hop, Interface).  

* **Next Hop**: refers to the next device (router or gateway) that a packet must go through to reach its destination.  
    - Firstly, when a router receives a packet, it checks the routing table to find the best route.  
    - Next, the router forwards the packet to the next hop based on the destination IP address.  
    - This process continues until the packet reaches its final destination.  

* **Interface**: is a connection point that allows a device (such as a router, switch, or computer) to communicate.  
    - Each interface has a unique IP address and is used to connect to a network or the internet.  
