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
windowSize = 5
newline = "\r\n\r\n"
my_list = []
seq = 0
file_requested = "1.mp4"#"John_Oliver_Quotations.mp4"

addr = ""
reply = ""
division_key = "divide_me_here"

def get_seq_number_as_int(string,divid):
	test = string.split(divid)
	return int(test[0])

def get_String(string,divid):
	test = string.split(divid)
	return test[1]



sentence = "Hello, From Client"
clientSocket = socket(AF_INET, SOCK_DGRAM)
sentence = "GET " + file_requested + " HTTP/1.1%s" % (newline)


clientSocket.sendto(sentence, (serverName, serverPort))

MSG = ""
reply= ""
dirr = os.path.dirname(file_requested)
output_file = open(file_requested, 'w')

recived = []

###############
for i in range (windowSize):
	reply, addr = clientSocket.recvfrom(1020)
	seq = get_seq_number_as_int(reply, division_key)
	recived.append(seq)
	reply = get_String(reply,division_key)
	MSG = MSG + reply

reply = ""	
print "Finished from FOR loop"
while len(recived) != 0:
	clientSocket.sendto(str(recived[0])+"_", (serverName, serverPort))
	recived.pop(0)
	
	print "waiting to recive: ", len(MSG), " : ", recived
	if (reply != "end"):
		MSG = MSG + reply
		reply, addr = clientSocket.recvfrom(1020)
		seq = get_seq_number_as_int(reply, division_key)
		recived.append(seq)
		reply = get_String(reply,division_key)
	
print "Finished from while loop", seq


output_file.write(MSG)
output_file.close()

print "out..."
print str(len(MSG))

clientSocket.close()
