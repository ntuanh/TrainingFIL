## Flow Control 
* Avoid overwhelming the receiver .
* Ensure that the sender does not overwhelm the receiver by sending data too quickly .
* How does work ?   The sender sends one packet and waits for an ACK (acknowledgment) from the receiver before sending the next packet .
* If the receiver does not receive a packet, it will send a NACK (negative acknowledgment) .
    * Sliding Window Flow Control ( TCP )
    * Stop-and-Wait 
    * Rate-based 
    * ECN ( Explicit congestion notification ) .

## Congestion control 
* Avoid overwhelming the network . 
* The sender should not send data too quickly, as this can lead to network congestion and packet loss
* How does work ?   