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
file_requested = "index.txt"

#sentence = ""
addr = ""
reply = ""

sentence = "Hello, From Client"
clientSocket = socket(AF_INET, SOCK_DGRAM)
sentence = "GET " + file_requested + " HTTP/1.1%s" % (newline)
#print sentence
clientSocket.settimeout(5)

i = 0
#while i < 5:
#	try:
		#sentence = raw_input('Client : ')
clientSocket.sendto(sentence, (serverName, serverPort))
try:
	reply, addr = clientSocket.recvfrom(1000)
	#print reply
	i = i + 1
	MSG = 'Enter your message to send here : '
except timeout:
	print "time is out ..."
	reply = "Nothing.."

dirr = os.path.dirname(file_requested)
#print dirr
#os.stat(dirr)
output_file = open(file_requested, 'w')
output_file.write(reply)
print "Receving %d bytes of data" % (len(reply))
output_file.close()
print "Recieved"
		
#clientSocket.sendto(sentence, (serverName, serverPort))

clientSocket.close()
