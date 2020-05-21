
import os
import time

def DDOS_Attack():

	clear = os.system('clear')

	print("")
	print("**************************************************************")
	print("*               Welcome to DDOS Attack system                *")
	print("**************************************************************")
	print("")
	print("                   (1) ICMP Flood Attack   ")
	print("")
	print("                   (2) UDP Flood Attack   ")
	print("")
	print("                   (3) SYN Flood Attack   ")
	print("")
	print("                   (4) DNS Flood Attack   ")
	print("")
	print("**************************************************************")
	print("*                        Author by SL                        *")
	print("**************************************************************")
	
	a = input("[DDOS@DDOS_Attack]#")
	a = int(a)
	time.sleep(1)
	try:
		if a == 1:
			try:
				from ICMP_Flood import process
				process()
			except KeyboardInterrupt:
				from ICMP_Flood import ICMP_Flood_End
				ICMP_Flood_End()
				DDOS_Attack()
		elif a == 2:
			try:
				from UDP_Flood import process 
				process()
			except KeyboardInterrupt:
				from UDP_Flood import UDP_Flood_End
				UDP_Flood_End()
				DDOS_Attack()
		elif a == 3:
			try:
				from SYN_Flood import process
				process()
			except KeyboardInterrupt:
				from SYN_Flood import SYN_Flood_End
				SYN_Flood_End()
				DDOS_Attack()
		elif a == 4:
			try:
				from DNS_Flood1 import process
				process()
			except KeyboardInterrupt:
				from DNS_Flood1 import DNS_Flood_End
				DNS_Flood_End()
				DDOS_Attack()
	except KeyboardInterrupt:
		print("Go back")
	
DDOS_Attack()