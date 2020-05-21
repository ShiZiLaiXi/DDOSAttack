import scapy.all as scapy
import sys
import time
import os


sys.path.append("/home/sss/scapy-test/Abnormal Message Detection/TCPprotocol")
sys.path.append("/home/sss/scapy-test/Abnormal Message Detection/IPprotocol")

def Abnormal_Message():
	clear = os.system('clear')

	print("")
	print("**************************************************************")
	print("*                   Welcome to DDOS Attack system            *")
	print("**************************************************************")
	print("")
	print("                   (1) IP Protocol Message Option    ")
	print("")
	print("                   (2) TCP Protocol Message Option    ")
	print("")
	print("**************************************************************")
	print("*                          Author by SL                      *")
	print("**************************************************************")

	a = input("[DDOS@Abnormal_Message]#")
	a = int(a)
	time.sleep(1)
	try:
		if a == 1:
			try:
				from IP_Protocol import IP_Protocol
				IP_Protocol()
			except KeyboardInterrupt:
				Abnormal_Message()
		elif a == 2:
			try:
				from TCP_Protocol import TCP_Protocol
				TCP_Protocol()
			except KeyboardInterrupt:
				Abnormal_Message()
	except KeyboardInterrupt:
		print("Go back")

Abnormal_Message()
