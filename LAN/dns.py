#!/usr/bin/python

from scapy.all import *


def find_dns(pkt):
    if pkt.haslayer(scapy.DNS):
        print(pkt[scapy.IP].src, pkt[scapy.DNS].summary())


if __name__ == "__main__":
    sniff(prn=find_dns)
