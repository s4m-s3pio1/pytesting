#!/usr/bin/env python

import subprocess
import optparse
import re


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="mention interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="mention new mac")
    (opts, arguments) = parser.parse_args()
    if not opts.interface:
        parser.error("[!] did not specify interface, use python main.py --help for instructions")
    elif not opts.new_mac:
        parser.error("[!] did not specify mac address, use python main.py --help for instructions")
    return opts


def mac_change(inf, mac):
    subprocess.call(["ifconfig", inf, "down"])
    subprocess.call(["ifconfig", inf, "hw", "ether", mac])
    subprocess.call(["ifconfig", inf, "up"])


def get_mac(inf):
    result = subprocess.check_output(["ifconfig", inf])
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)
    if mac_result:
        return str(mac_result.group(0))
    else:
        print("[!]couldn't find mac address")


options = get_args()
interface = options.interface
new_mac = options.new_mac

current_mac = get_mac(interface)
print("current mac address: "+str(current_mac))

print("[+] changing mac address of "+interface+" to "+new_mac)

mac_change(interface, new_mac)

current_mac = get_mac(interface)
print("current mac address: "+str(current_mac))
                                                
