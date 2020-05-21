
import time
import os

def TCP_Protocol():

	clear = os.system('clear')
	print("")
	print("**************************************************************")
	print("*                  Welcome to DDOS Attack system             *")
	print("**************************************************************")
	print("")
	print("                   (1) SYN Data Slice Transmission     ")
	print("")
	print("                   (2) TCP All Flags All Zero  ")
	print("")
	print("                   (3) FIN SYN Flags All One  ")
	print("")
	print("                   (4) Only FIN Is One  ")
	print("")
	print("**************************************************************")
	print("*                          Author by SL                      *")
	print("**************************************************************")

	a = input("[Abnormal_Message@TCP]#")
	a = int(a)
	time.sleep(1)

	try:
		if a == 1:
			try:
				from SYN_Fragment import Syn_fragment
				Syn_fragment()
			except KeyboardInterrupt:
				TCP_Protocol()
		elif a == 2:
			try:
				from TCP_AllFlags_zero import TCP_Zero
				TCP_Zero()
			except KeyboardInterrupt:
				TCP_Protocol()
		elif a == 3:
			try:
				from FIN_SYN_One import FIN_SYN_One
				FIN_SYN_One()
			except KeyboardInterrupt:
				TCP_Protocol()
		elif a == 4:
			try:
				from FIN_Only_one import FIN_One
				FIN_One()
			except KeyboardInterrupt:
				TCP_Protocol()		
		
	except KeyboardInterrupt:
		print("Go back")

TCP_Protocol()