#|/usr/bin/python

import thread
from include.server import server

def client(self):
	global client1
	client1 = server(5555)

thread.start_new_thread(client, (None,))
client2 = server(5554)

while 1:
	file_name = client1.recv_file_name()
	file_size = client1.recv_file_size()
	file_lines = client1.recv_file_lines()
	
	print file_name
	print file_size
	print file_lines
	
	client2.set_control_acceptance()
	client2.send_file_name(file_name)
	client2.send_file_size(file_size)
	client2.send_file_lines(file_lines)
 
	if client2.control_acceptance() == True:
		client1.send_control_acceptance(True)
		while 1:
			line = client1.recv_file(file_size)
			if line[0] == True:
				client2.send_file(line[1])
			else:
				break
	else:
		client1.send_control_acceptance(False)
		
	client1.close()
	client2.close()
	
	break


