from scapy.all import *
import socket



s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
s.bind(("eth0", 0))
pe=Ether()/IP(src="172.10.10.10",dst="10.10.10.186")/ICMP()
data = pe.build()
while True:
    print("pkt sent")
    s.send(data)
