import os
from HTMLParser import HTMLParser
from socket import *
import time
import sys
import struct
import thread
import threading



serverName = '127.0.0.1'
serverPort = 14000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))



while True:
	print "Server is ready to receive..."
	MSG, addr = serverSocket.recvfrom(1000)
	print "received message is : ", MSG
	method = MSG.split(' ')[0]
	my_file = MSG.split(' ')
	my_file = my_file[1] 
	print "file is :" + my_file
	open_file = open(my_file,'rb')
	if (method == 'GET'):
		file_content = open_file.read() 
	open_file.close()

	serverSocket.sendto(file_content , addr)

serverSocket.close()
