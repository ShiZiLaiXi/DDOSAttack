
import os
import time

def Scan():

	clear = os.system('clear')

	print("")
	print("**************************************************************")
	print("*                 Welcome to DDOS Attack system              *")
	print("**************************************************************")
	print("")
	print("                         (1) IP Scan     ")
	print("")
	print("                         (2) Port Scan  ")
	print("")
	print("**************************************************************")
	print("*                         Author by SL                       *")
	print("**************************************************************")

	a = input("[DDOS@Scan Protection]#")
	a = int(a)
	time.sleep(1)
	try:
		if a == 1:
			try:
				from IP_Scan import process
				process()
			except KeyboardInterrupt:
				from IP_Scan import IP_Scan_End
				IP_Scan_End()
				Scan()
		elif a ==2:
			try:
				from Port_Scan import process
				process()
			except KeyboardInterrupt:
				from Port_Scan import Port_Scan_End
				Port_Scan_End()
				Scan()
	except KeyboardInterrupt:
		print("Go back")
	
Scan()