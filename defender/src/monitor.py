from scapy.all import *
import wifi


def Search():
    wifilist = []

    cells = wifi.Cell.all('wlan0')

    for cell in cells:
        wifilist.append(cell)

    return wifilist

def handler(packet):
    print(packet.summary())



if __name__ == "__main__":
    Search()
    

    #sniff(iface="eth0", prn=handler, store=0)
