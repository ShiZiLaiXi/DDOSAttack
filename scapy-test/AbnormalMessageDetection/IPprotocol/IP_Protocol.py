import scapy.all as scapy

import time
import os

def IP_Protocol():
	
	clear = os.system('clear')
	print("")
	print("**************************************************************")
	print("*                  Welcome to DDOS Attack system             *")
	print("**************************************************************")
	print("")
	print("                   (1) Wrong IP Message Options     ")
	print("")
	print("                   (2) IP TimeStamp Message Options  ")
	print("")
	print("                   (3) IP Security Message Options  ")
	print("")
	print("                   (4) IP Data Flow Message Options  ")
	print("")
	print("                   (5) IP Route Message Options  ")
	print("")
	print("                   (6) IP Strict Route Message Options  ")
	print("")
	print("                   (7) IP Loose Route Message Options  ")
	print("")
	print("**************************************************************")
	print("*                          Author by SL                      *")
	print("**************************************************************")

	a = input("[Abnormal_Message@IP]#")
	a = int(a)
	time.sleep(1)
	try:
		if a== 1:
			try:
				from Wrong_IP import Wrong_IP
				Wrong_IP()
			except KeyboardInterrupt:
				IP_Protocol()
		elif a == 2:
			try:
				from IP_TimeStamp import IP_TimeStamp
				IP_TimeStamp()
			except KeyboardInterrupt:
				IP_Protocol()
		elif a == 3:
			try:
				from IP_Security import IP_Security
				IP_Security()
			except KeyboardInterrupt:
				IP_Protocol()
		elif a == 4:
			try:
				from IP_Data_Flow import IP_Data_Flow
				IP_Data_Flow()
			except KeyboardInterrupt:
				IP_Protocol()
		elif a == 5:
			try:
				from IP_Route import IP_Route
				IP_Route()
			except KeyboardInterrupt:
				IP_Protocol()
		elif a == 6:
			try:
				from IP_Strict_Route import IP_Strict_Route
				IP_Strict_Route()
			except KeyboardInterrupt:
				IP_Protocol()
		elif a == 7:
			try:
				from IP_Loose_Route import IP_Loose_Route
				IP_Loose_Route()
			except KeyboardInterrupt:
				IP_Protocol()
	except KeyboardInterrupt:
		print("Go back")


IP_Protocol()