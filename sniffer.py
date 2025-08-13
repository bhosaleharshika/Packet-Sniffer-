from scapy.all import sniff

# Function to process each packet
def packet_callback(packet):
    print(packet.summary())

# Start sniffing
print("Starting packet capture... Press CTRL+C to stop.")
sniff(prn=packet_callback, count=20)  # Capture 20 packets
