"""Python3 code to scan and list the ports for a given network"""

#nmap - Network Mapper
import nmap

def main():
	nm = nmap.PortScanner()

	host_net = input("Enter the host network: ")

	#scans the host for ports within the specified range
	nm.scan(str(host_net),'21-443')

	#all_hosts() - gives all hosts associated with the network
	for host in nm.all_hosts():
		#prints host IP with address
		print('Host : %s (%s)' %(host,nm[host].hostname()))
		#state of the host(up/close)
		print('State : %s' %(nm[host].state()))


		#for each protocol associated with the port
		for each_proto in nm[host].all_protocols():
			print("-----------")
			print("Protocol : %s" %each_proto)

			#keys() - returns all the active ports avalaible
			lport = nm[host][each_proto].keys()

			for i in sorted(lport,reverse=True):
				#prints status of each port
				print('port: %s  state: %s' %(i,nm[host][each_proto][i]['state']))


if __name__ == '__main__':
	main()