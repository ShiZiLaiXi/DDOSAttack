import scapy.all as scapy
import os
import time


def Packet_based():
	clear = os.system('clear')
	print("")
	print("**************************************************************")
	print("*                 Welcome to DDOS Attack system              *")
	print("**************************************************************")
	print("")
	print("                   (1) Unknow Protocol Type    ")
	print("")
	print("                   (2) Tear Drop   ")
	print("")
	print("                   (3) IP Data Fragment   ")
	print("")
	print("                   (4) LAND Attack   ")
	print("")
	print("                   (5) WinNuke Attack   ")
	print("")
	print("                   (6) Smurf Attack   ")
	print("")
	print("                   (7) Super ICMP Dat  Attack   ")
	print("")
	print("**************************************************************")
	print("*                        Author by SL                        *")
	print("**************************************************************")
	
	a = input("[DDOS@Packet_based]#")
	a = int(a)
	time.sleep(1)
	try:
		if a == 1:
			try:
				from UnknownProtocolType import UnProtoType
				UnProtoType()
			except KeyboardInterrupt:
				Packet_based()
		elif a == 2:
			try:
				from TearDrop import TearDrop
				TearDrop()
			except KeyboardInterrupt:
				Packet_based()
		elif a == 3:
			try:
				from IP_Data_Fragment import IP_Data
				IP_Data()
			except KeyboardInterrupt:
				Packet_based()
		elif a == 4:
			try:
				from LANDattack import LandAttack
				LandAttack()
			except KeyboardInterrupt:
				Packet_based()
		
		elif a == 5:
			try:
				from WinNukeAttack import WinNuke
				WinNuke()
			except KeyboardInterrupt:
				Packet_based()
		elif a == 6:
			try:
				from SmurfAttack import Smurf
				Smurf()
			except KeyboardInterrupt:
				Packet_based()
		elif a == 7:
			try:
				from Ping_of_death import Ping_attack
				Ping_attack()
			except KeyboardInterrupt:
				Packet_based()

	except KeyboardInterrupt:
		print("Go back")


Packet_based()