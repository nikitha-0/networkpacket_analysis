import pyshark
from collections import defaultdict
cap=pyshark.FileCapture('data/youtube.pcapng',keep_packets=False)
ip_count=defaultdict(int)
for packet in cap:
    if 'IP' in packet:
        ip_count[packet.ip.src]+=1
print('\nPacket count per IP:\n')
for ip,count in ip_count.items():
    print(ip,"->",count,"packets")
