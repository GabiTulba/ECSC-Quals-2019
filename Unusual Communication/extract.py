from scapy.all import *


packets=rdpcap('captura.pcapng')

ping_packets = []

for packet in packets:
	if 'ICMP' in packet.summary() and 'reply' in packet.summary():
		ping_packets.append(packet.load)

ping_data = ''.join(ping_packets)

with open('flag.png','wb') as f:
	f.write(ping_data)
