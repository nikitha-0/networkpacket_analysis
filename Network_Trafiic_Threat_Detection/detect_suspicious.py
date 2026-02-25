import pyshark
from collections import defaultdict
cap=pyshark.FileCapture('data/youtube.pcapng',keep_packets=False)
ip_count=defaultdict(int)
for packet in cap:
    if 'IP' in packet:
        ip_count[packet.ip.src]+=1
THRESHOLD=30
print("\n Suspicious IP Detection:\n")
for ip,count in ip_count.items():
    if count>THRESHOLD:
        print(f"[ALERT]{ip}->{count}packets")
    else:
        print(f"[NORMAL]{ip}->{count}packets")
suspicious_ips=[]
for ip,count in ip_count.items():
    if count>20 and not ip.startswith("192.168"):
        suspicious_ips.append(ip)
print("\nSuspicious IPs detected:")
for ip in suspicious_ips:
    print(ip)
with open("suspicious_ips.txt","w")as f:
    f.write("Suspicious IPs Detected:\n")
    for ip in suspicious_ips:
        f.write(ip+"\n")
print("\n Suspicious IPs saved to suspicious_ips.txt")