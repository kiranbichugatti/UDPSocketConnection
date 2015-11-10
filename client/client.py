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
file_requested = "index.html"#"John_Oliver_Quotations.mp4"

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
MSG = ""
reply= ""
dirr = os.path.dirname(file_requested)
output_file = open(file_requested, 'w')
while 1:	
	try:
		if (reply != "*X*"):
			#MSG = MSG + reply
			reply, addr = clientSocket.recvfrom(1000)
			#print "_" + reply
			#reply = bytes.decode(reply)
			output_file.write(reply)
		else:
			break
	except timeout:
		print "time is out ..."
		#print MSG
		reply = "Nothing.."
		break


#print dirr
#os.stat(dirr)


output_file.close()

#	except clientSocket.error:
#		print "Error timeout..."
print "out..."
		
        



#clientSocket.sendto(sentence, (serverName, serverPort))


clientSocket.close()
