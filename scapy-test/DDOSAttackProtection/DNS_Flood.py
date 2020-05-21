import scapy.all as scapy 
import time
from multiprocessing import Pool
import os

def DNS_Flood(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    time.sleep(3)
    print('Task %s runs 3 seconds.' % (name))

if __name__ == '__main__':
	p = Pool(3)
	for i in range(4):
		p.apply_async(DNS_Flood,args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')

#DNS_Flood(process_id)
