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



#while True:
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
print "length is :" + str(len(file_content))
size = len(file_content) 
open_file.close()
loop = 0
done = 0
i=0
while (i <= len(file_content)):
	#print i
	loop = loop + 1
	string = file_content[i : i+1000]
	#string = string.decode('cp1252')
	#string = unicode(string, errors='ignore')
#	if (i+1000 > len(file_content)):
#		i = i + ( len(file_content) - i )
#		done = 1
#	else:
	i = i + 1000
	#print "Sending: " + string
	serverSocket.sendto(string , addr)

	#time.sleep(0.01)

i = i + ( len(file_content) - i )
string = file_content[i : i + 1000]
#string = unicode(string, 'utf-8')
#string = string.encode('utf-8')
serverSocket.sendto(string , addr)
#print "exit"
print i
print "loop is :", loop
serverSocket.sendto('uiowa' , addr)
serverSocket.close()
