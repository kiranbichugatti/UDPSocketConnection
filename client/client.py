import os
from HTMLParser import HTMLParser
from socket import *
import time
import sys
import struct
import thread
import threading
import hashlib

serverName = '127.0.0.1'
serverPort = 14000

newline = "\r\n\r\n"
my_list = []
file_requested = "1.mp3"#John_Oliver_Quotations.mp4"

md5 = hashlib.md5()
#sentence = ""
addr = ""
reply = ""

sentence = "Hello, From Client"
clientSocket = socket(AF_INET, SOCK_DGRAM)
sentence = "GET " + file_requested + " HTTP/1.1%s" % (newline)
#print sentence
#clientSocket.settimeout(5)

i = 0
#while i < 5:
#	try:
		#sentence = raw_input('Client : ')
clientSocket.sendto(sentence, (serverName, serverPort))
MSG = ""
reply= ""
dirr = os.path.dirname(file_requested)
output_file = open(file_requested, 'w')

loop = 0
while 1:	
	try:
		if (reply != 'uiowa'):
			MSG = MSG + reply
			
			#MSG = MSG + reply
			loop = loop + 1
			reply, addr = clientSocket.recvfrom(1000)
			if (len(reply) < 1000):
				#md5.update(reply)
				print "reply:", reply
				#print "md5:", md5.hexdigest()
			#print "_" + reply
			#reply = bytes.decode(reply)

		else:
			break
	except:
		print "time is out ..."
		#print MSG
		reply = "Nothing.."
		break


#print dirr
#os.stat(dirr)
md5.update(MSG)
print "md5:", md5.hexdigest()
output_file.write(MSG)
output_file.close()

#	except clientSocket.error:
#		print "Error timeout..."
print "out..."
print "loop is :", loop
#print str(len(MSG))
		
        



#clientSocket.sendto(sentence, (serverName, serverPort))


clientSocket.close()
