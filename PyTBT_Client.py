#|/usr/bin/python

from include.client import client

server = '127.0.0.1'

choise = int(raw_input('1 -> Send a file\n2 -> Recv a file\n> '))

if choise == 1:
	conn = client(server, 5555, 1)
	dir = raw_input ('Insert the directory\n> ')

	conn.send_file_name(dir)	
	conn.send_file_size(dir)
	conn.send_file_lines(dir)

	try:
		control_acceptance = conn.recv_control_acceptance()
		if control_acceptance == True:
			conn.send_file(dir)
			
		elif control_acceptance == False:
			print 'File denied!'
	except IOError:
		print 'Error!'
		
elif choise == 2:
	conn = client(server, 5554, 0)

	control = raw_input('> ')

	if conn.control_acceptance(control):
		file_name = conn.recv_file_name()
		file_size = conn.recv_file_size()
		file_lines = conn.recv_file_lines()
		
		print file_name
		print file_size
		print file_lines
		
		print 'Waiting...'
		conn.recv_file(file_name, file_size, file_lines)
		print 'Finished!'
else:
	print 'Error!\n'
