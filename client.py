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

newline = "\r\n\r\n"
my_list = []
file_requested = "index.html"

#sentence = ""
addr = ""
reply = ""

sentence = "Hello, From Client"
clientSocket = socket(AF_INET, SOCK_DGRAM)


i = 0
while i < 3:
	try:
		sentence = raw_input('Client : ')
		clientSocket.sendto(sentence, (serverName, serverPort))         
		reply, addr = clientSocket.recvfrom(1024)
		print reply
		i = i + 1
		MSG = 'Enter your message to send here : '
	except Exception, e:
		raise e
		break
print "out..."
		
        



#clientSocket.sendto(sentence, (serverName, serverPort))


clientSocket.close()
