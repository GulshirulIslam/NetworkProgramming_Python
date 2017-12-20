"""Python2 code - prints Source and Destination IP from the given 
 'pcap' file (file can be obtained from wireshark ) """

#using dpkt python module
import dpkt
import socket

def printPcap(pcap):

	#ts - timestamp , buf - buffer
	for ts,buf in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data

			#read the source and dest IP adresses 
			src_ip = socket.inet_ntoa(ip.src) #get decimal internet source address
			dst_ip = socket.inet_ntoa(ip.dst) #get decimal internet destination address

			print 'Source: ' +src_ip +'\tDestination: ' +dst_ip

		except:
			pass

def main():

	#.pcap file present in PWD
	f = open('sample.pcap')

	#variable 'pcap' holds all the data from the pcap file
	pcap = dpkt.pcap.Reader(f)

	printPcap(pcap)


if __name__ == '__main__':
	main()
