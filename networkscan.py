#!/usr/bin/env python

import scapy.all as scapy
import optparse


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="ip_input", help="mention target's ip to search for mac address")
    (opts, arguments) = parser.parse_args()
    if not opts.ip_input:
        parser.error("[!] did not specify interface, use python main.py --help for instructions")
    return opts


def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broad = broadcast/arp_req
    answered_list = scapy.srp(arp_req_broad, timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def res_print(res_list):
    print("IP\t\t\tMAC ADDR\n--------------------------------------------")
    for client in res_list:
        print(client["ip"]+"\t\t"+client["mac"])


options = get_args()
results = scan(options.ip_input)
res_print(results)
                      
