import time  # Import time module for delays
import random  # Import random module to simulate packet loss

def congestion_control_simulation():
    print("\n=== Congestion Control Simulation ===")  
    
    total_packets = 20  # Total number of packets to send
    cwnd = 1  # Initial Congestion Window (cwnd) size
    ssthresh = 8  # Slow Start threshold (ssthresh)
    sent_packets = 0  # Counter for sent packets
    
    while sent_packets < total_packets:
        window_size = min(cwnd, total_packets - sent_packets)  # Determine how many packets can be sent
        print(f"Sending packets {sent_packets + 1} to {sent_packets + window_size} (cwnd = {cwnd})...")
        
        time.sleep(1)  # Delay to simulate transmission
        acks = []  # List to store acknowledged packets
        loss_occurred = False  # Flag to detect packet loss
        
        for i in range(sent_packets + 1, sent_packets + window_size + 1):
            if random.random() < 0.2:  # 20% chance of packet loss
                print(f"Packet {i} lost! Congestion detected.")  
                loss_occurred = True  # Set congestion flag
            else:
                print(f"Packet {i} acknowledged.")  
                acks.append(i)  # Store acknowledged packet
        
        if loss_occurred:  
            print("Congestion detected! Reducing window size.")  
            ssthresh = max(cwnd // 2, 1)  # Reduce ssthresh to half of cwnd
            cwnd = 1  # Reset cwnd to 1 (Slow Start phase)
        else:
            if cwnd < ssthresh:  
                cwnd *= 2  # Slow Start: Double cwnd  
            else:
                cwnd += 1  # Congestion Avoidance: Increase cwnd linearly
        
        sent_packets = max(acks, default=sent_packets)  # Update the next packet to send
        time.sleep(1)  # Delay before the next transmission cycle

if __name__ == "__main__":
    congestion_control_simulation()  # Run the simulation
