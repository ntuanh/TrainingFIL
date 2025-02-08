import time
import random

def stop_and_wait_simulation():
    print("\n=== Stop-and-Wait Flow Control Simulation ===")
    for packet in range(1, 6):  # Sending 5 packets
        print(f"Sending Packet {packet}...")
        time.sleep(1)
        
        if random.random() < 0.2:  # Simulating packet loss (20% chance)
            print(f"Packet {packet} lost! Retransmitting...")
            time.sleep(1)
            print(f"Packet {packet} re-sent and acknowledged.")
        else:
            print(f"Packet {packet} acknowledged.")
        
        time.sleep(1)

def sliding_window_simulation(window_size=3):
    print("\n=== Sliding Window Flow Control Simulation ===")
    total_packets = 10
    sent_packets = 0
    
    while sent_packets < total_packets:
        window_end = min(sent_packets + window_size, total_packets)
        print(f"Sending packets {sent_packets + 1} to {window_end}...")
        
        time.sleep(1)
        acks = []
        for i in range(sent_packets + 1, window_end + 1):
            if random.random() < 0.5:  # Simulating packet loss
                print(f"Packet {i} lost!")
            else:
                print(f"Packet {i} acknowledged.")
                acks.append(i)
        
        if len(acks) == 0:
            print("No packets were acknowledged. Resending the entire window...")
        else:
            sent_packets = max(acks)  # Move window to the last acknowledged packet
        
        time.sleep(1)

if __name__ == "__main__":
    #stop_and_wait_simulation()
    sliding_window_simulation()
