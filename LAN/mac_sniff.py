#!/usr/bin/python

import socket
from struct import *


def address(addr):
    temp = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (
        ord(addr[0]),
        ord(addr[1]),
        ord(addr[2]),
        ord(addr[3]),
        ord(addr[4]),
        ord(addr[5]),
    )
    return temp


if __name__ == "__main__":
    try:
        sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    except:
        print("!! Socket creation error.")
        exit(0)
    while True:
        pkt = sock.recvfrom(65535)
        pkt = pkt[0]
        eth_len = 14
        eth_head = pkt[:eth_len]
        eth = unpack("!6s6sH", eth_head)
        eth_procol = socket.ntohs(eth[2])
        print(f"<> Destination MAC: {address(pkt[:6])}", end="")
        print(f"<> Source MAC: {address(pkt[6:12])}", end="")
        print(f"<> Protocol: {str(eth_procol)}")
