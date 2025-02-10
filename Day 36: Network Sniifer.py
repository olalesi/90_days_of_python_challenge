from scapy.all import sniff, wrpcap, IP, TCP, UDP

# List to store captured packets
captured_packets = []

def process_packet(packet):
    """Processes and logs packet details."""
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "Other"

        print(f"Source: {src_ip} → Destination: {dst_ip} | Protocol: {protocol}")

        # Add packet to the list for saving
        captured_packets.append(packet)

# Capture packets (change count=None for continuous sniffing)
print("[*] Starting packet capture...")
sniff(filter="ip", prn=process_packet, store=False, count=50)  # Captures 50 packets

# Save packets to a PCAP file
pcap_filename = "captured_traffic.pcap"
wrpcap(pcap_filename, captured_packets)
print(f"[*] Packets saved to {pcap_filename}")
