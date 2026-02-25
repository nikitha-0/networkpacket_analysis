import pyshark
cap=pyshark.FileCapture('data/youtube.pcapng',keep_packets=False)
count=0
for packet in cap:
    if 'IP' in packet:
        print(packet.ip.src,"->",packet.ip.dst)
        count+=1
    if count==10:
        break
print("\nIP extraction completed")
