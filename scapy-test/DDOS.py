#coding:utf-8
import scapy.all as scapy
import time
import sys
#from LANDattack import LandAttack
#from Ping_of_death import Ping_attack
import os

sys.path.append('/home/sss/scapy-test/ARP_Flood')
sys.path.append("/home/sss/scapy-test/ScanProtection")
sys.path.append("/home/sss/scapy-test/DDOSAttackProtection")
sys.path.append("/home/sss/scapy-test/Packet-basedAttack")
sys.path.append("/home/sss/scapy-test/AbnormalMessageDetection")

def  ddos():

	clear = os.system('clear')

	print("")
	print("**************************************************************")
	print("*                 Welcome to DDOS Attack system              *")
	print("**************************************************************")
	print("")
	print("                 (1) ARP_Flood Attack Protection    ")
	print("")
	print("                 (2) Scan Protection   ")
	print("")
	print("                 (3) DDOS Attack Protection   ")
	print("")
	print("                 (4) Packet-based Attack   ")
	print("")
	print("                 (5) Abnormal Message Detection   ")
	print("")
	print("**************************************************************")
	print("*                       Author by SL                         *")
	print("**************************************************************")

	a = input("[DDOS]#")
	a = int(a)
	time.sleep(1)
	try:
		if a == 1:
			try:
				from ARP_Flood import Arp_flood
				Arp_flood()
			except KeyboardInterrupt:
				ddos()

		elif a == 2:
			try:
				from Scan_Protection import Scan
				Scan()
			except KeyboardInterrupt:
				ddos()
		elif a == 3:
			try:
				from DDOS_Attack_Protection import DDOS_Attack
				DDOS_Attack()
			except KeyboardInterrupt:
				ddos()

		elif a==4:
			try:
				from Packet_based import Packet_based
				Packet_based()
			except KeyboardInterrupt:
				ddos()
		elif a==5:
			try:
				from Abnormal_Message import Abnormal_Message
				Abnormal_Message()
			except KeyboardInterrupt:
				ddos()
	except KeyboardInterrupt:
		print("quit")
ddos()
