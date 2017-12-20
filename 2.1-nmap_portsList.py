""" Python3 code- scans and displays the status of the port of the specified 
network [argparse is used]"""

"""usage python3 filename.py --host host_ip --port port_number"""

#nmap - Network Mapper
import nmap
import argparse

def main():
	nm = nmap.PortScanner()

	parser = argparse.ArgumentParser()
	parser.add_argument('--host',dest = 'host',required = True)
	parser.add_argument('--port',dest = 'port',required = True)

	args = parser.parse_args()

	host_net = args.host
	port = args.port

	#scans the host for ports
	nm.scan(str(host_net),port)

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
				#prints status of the user entered port (either up or close)
				print('port: %s  state: %s' %(i,nm[host][each_proto][i]['state']))

if __name__ == '__main__':
	main()