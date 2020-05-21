import scapy.all as scapy
import os


def IP_Route():

	clear = os.system('clear')

	print("**************************************")
	print("            IP_Record_Route")
	print("**************************************")

	print("Please input your target's IP")
	target = input("[IP_Record_Route]#")
	src_ip = scapy.RandIP()
	num =0
	try:
		while True:
			packet= scapy.IP(src=src_ip,dst=target,ttl=128,options=scapy.IPOption_RR(copy_flag=0,length=39,routers=['0.0.0.0', '0.0.0.0', '0.0.0.0', '0.0.0.0', '0.0.0.0', '0.0.0.0', '0.0.0.0', '0.0.0.0', '0.0.0.0']))/scapy.ICMP()/scapy.Raw(load=b'abcdefghijklmnopqrstuvwabcdefghi')
			scapy.send(packet,verbose=False)
			num += 1
			print("Sent "+str(num)+"packets")
	except KeyboardInterrupt:
		print("Ctrl + C  detected......")
	
IP_Route()