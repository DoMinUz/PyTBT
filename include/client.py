#!/usr/bin/python

import socket
import os
import stat

class client:
	
	def __init__(self, ip, port, client):
		self.sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect ((ip, port))
		self.percentage = 0
		if client == 0:
			print self.sock.recv(5)
		else:
			pass


	def send_file_name(self, dir):
		file_name = dir.split('/')[-1]
		self.sock.send(str(len(str(len(file_name)))))
		self.sock.send(str(len(file_name)))
		self.sock.send(file_name)


	def send_file_size(self, dir):
		file_size = str(os.stat(dir)[stat.ST_SIZE])
		self.sock.send(str(len(file_size)))
		self.sock.send(file_size)


	def recv_file_name(self):
		len_file_len = self.sock.recv(1)
		file_len = self.sock.recv(int(len_file_len))
		return self.sock.recv(int(file_len))


	def recv_file_size(self):
		file_len = self.sock.recv(1)
		return self.sock.recv(int(file_len))


	def send_file_lines(self, dir):
		file_lines = len(open(dir, 'r').readlines())
		self.sock.send(str(len(str(file_lines))))
		self.sock.send(str(file_lines))


	def recv_file_lines(self):
		file_lines = self.sock.recv(1)
		return self.sock.recv(int(file_lines))


	def send_file(self, dir):
		split_file = open(dir, 'r').readlines()
		file_lines, i = len(split_file), 0
		for line in split_file:
			self.sock.send(line)
			i += 1.
			percents = str(int(i/file_lines * 100))
			if os.name == 'posix':
				os.system('clear')
			elif os.name == 'nt':
				os.system('cls')
			print percents + '%'


	def recv_file(self, file_name, byte, file_lines):
		self.recv_file = open(file_name, 'w')
		byte, file_lines = int(byte), int(file_lines)
		i = 0

		while 1:
			data = self.sock.recv(byte)
			i += 1.
			percents = str(int(i/file_lines * 100))
			print percents + '%'
			
#			if os.name == 'posix':
#				os.system('clear')
#			elif os.name == 'nt':
#				os.system('cls')
			if data:
				self.recv_file.write(data)
			else:
				break


	def control_acceptance(self, data):
		if data == 'y':
			self.sock.send('y')
			return True
		elif data == 'n':
			self.sock.send('n')
			return False
		else:
			return 'Error'


	def recv_control_acceptance(self):
		data = self.sock.recv(1)

		if data == 'y':
			return True
		elif data == 'n':
			return False
		else:
			return 'Error'


	def __del__(self):
		try:
			self.recv_file.close()
			self.sock.close()
		except AttributeError:
			pass

