import csv
import matplotlib.pyplot as plt
ips=[]
counts=[]
with open("live_suspicious_ips.csv","r") as f:
    reader=csv.DictReader(f)
    for row in reader:
        ips.append(row["IP Address"])
        counts.append(int(row["Packet Count"]))
plt.figure(figsize=(10,5))
plt.bar(ips,counts)
plt.xlabel("Suspicious IP Address")
plt.ylabel("Packet count")
plt.title("Live Traffic - Suspicious IPs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()