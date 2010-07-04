#!/usr/bin/python

import socket

class server:
	
	def __init__(self, port):
		self.sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind(("0.0.0.0", port))
		self.sock.listen(5)
		self.connection, self.address = self.sock.accept()


	def set_control_acceptance(self):
		self.connection.send('[y/n]')
		self.data = self.connection.recv(1)
		return True


	def control_acceptance(self):
		if self.data == 'y':
			return True
		elif self.data == 'n':
			return False
		else:
			return 'Error!'


	def send_control_acceptance(self, _bool):
		if _bool == True:
			self.data = 'y'
		else:
			self.data = 'n'

		if self.data == 'y':
			self.connection.send('y')
		elif self.data == 'n':
			self.connection.send('n')
		else:
			self.connection.send('E')

		return True


	def recv_file_name(self):
		len_digits_file_len = self.connection.recv(1)
		file_len = self.connection.recv(int(len_digits_file_len))
		file_name = self.connection.recv(int(file_len))
		return file_name

	def send_file_name(self, file_name):
		self.connection.send(str(len(str(len(file_name)))))
		self.connection.send(str(len(file_name)))
		self.connection.send(file_name)


	def recv_file_size(self):
		file_len = self.connection.recv(1)
		return self.connection.recv(int(file_len))
		

	def send_file_size(self, file_size):
		self.connection.send(str(len(file_size)))
		self.connection.send(file_size)


	def send_file_lines(self, file_lines):
		self.connection.send(str(len(file_lines)))
		self.connection.send(file_lines)


	def recv_file_lines(self):
		len_digits_file_lines = self.connection.recv(1)
		file_lines = self.connection.recv(int(len_digits_file_lines))
		return file_lines


	def recv_file(self, byte):
		self.byte = int(byte)
		line = self.connection.recv(self.byte)
		
		if line:
			return True, line
		else:
			return False, ''
	
	
	def send_file(self, line):
		self.connection.send(line)
	

	def close(self):
		self.sock.close()
		self.connection.close()
