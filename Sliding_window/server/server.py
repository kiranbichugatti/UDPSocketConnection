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
windowSize = 5 # 0~4 = 5
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))


def split_the_content(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ]


def get_seq_number_as_int(string,divid):
	test = string.split(divid)
	return int(test[0])


print "Server is ready to receive..."
MSG, addr = serverSocket.recvfrom(1017)
print "received message is : ", MSG
method = MSG.split(' ')[0]
my_file = MSG.split(' ')
my_file = my_file[1] 


print "file is :" + my_file
open_file = open(my_file,'rb')
if (method == 'GET'):
	file_content = open_file.read() 
print "length is :" + str(len(file_content))
open_file.close()
content_array = []
content_array = split_the_content(file_content,1000) # return an array basid on the content


size_of_array = len(content_array) 

division_key = "divide_me_here"

nxt = 0

#########
for i in range (windowSize):
	string = str(nxt) + division_key + content_array[nxt]
	serverSocket.sendto(string , addr)
	nxt = nxt + 1

print "Finished from FOR loop"

while True:
	ACK, addr = serverSocket.recvfrom(1018)
	ACK = get_seq_number_as_int(ACK,"_")
	if (ACK >= 0 and ACK != (size_of_array - 1)):
		#print "ACK = ", ACK, " : ",len(file_content) 
		if (nxt <= (size_of_array -1)):
			string = str(nxt) + division_key + content_array[nxt]
			print "sending..", len(string)
			serverSocket.sendto(string , addr)
			last = nxt
			nxt = nxt + 1
		else:
			string = "0" + division_key + "end"
			serverSocket.sendto(string , addr)
	else:
		print "exit from while"
		break



print "Finished from while loop, File size", len(file_content)
print last , " :: ", len(content_array[size_of_array -1]), " :: ", len(content_array[size_of_array -2])

serverSocket.sendto('0'+division_key+'uiowa' , addr)

serverSocket.close()
