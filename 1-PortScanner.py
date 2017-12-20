""" The fundamental step to enter a system is to scan the system's open ports"""

""" Python3 code gives status of the entered port (open/close) of the target IP"""

import socket

def main():
	host = input("Enter the host to be scanned: ")
	host_ip = socket.gethostbyname(host)

	#host_ip = input("Enter the ip: ")

	print(host_ip)

	choice = 'y'
	while(choice == 'y'):
		host_port = int(input("Enter the port to be scanned: "))

		try:
			s = socket.socket()
			s.connect((host_ip,host_port))
			print("port {} is open" .format(host_port))
			s.close()

		except:
			#if connection failed to establish indicates port closed
			print("port {} is closed" .format(host_port))

		choice = input("Do you want to continue(y/n): ")
		
	print("Port scanning completed")


if __name__ == '__main__':
	main()