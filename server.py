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
	MSG, addr = serverSocket.recvfrom(1024)
	print "received message is : ", MSG
	reply = raw_input('Server : ')
	serverSocket.sendto(reply , addr)

serverSocket.close()
