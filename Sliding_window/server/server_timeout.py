import os
from HTMLParser import HTMLParser
from socket import *
import time
import sys
import struct
import thread
import threading



serverName = '127.0.0.1'
serverPort = 14010
windowSize = 5 # 0~4 = 5
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))


def split_the_content(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ]


def get_seq_number_as_int(string,divid):
	test = string.split(divid)
	return int(test[0])

def len_check(arr,num):
	while len(arr) < (num + 1):
		arr.append("asnobi")

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
seq_chk = []
time_out = []
pick =[] 
def test_resend(str_):
	serverSocket.settimeout(None)
	#print "There is an Error with packet after ", str_
	pck = int(str_) 
	string = str(pck) + division_key + content_array[pck ]
	print "Resending..", pck
	serverSocket.sendto(string , addr)
	time_out.append([pck,time.time()])
	#print "Lost pck has been sent"

size_of_array = len(content_array) 

division_key = "divide_me_here"

nxt = 0

#########
for i in range (windowSize):
	string = str(nxt) + division_key + content_array[nxt]
	ACK = nxt
	
	len_check(seq_chk,ACK)
	seq_chk[ACK]  = "XXX"

	serverSocket.sendto(string , addr)
	time_out.append([ACK,time.time()])
	nxt = nxt + 1


print "Finished from FOR loop"
final = "no"

while True:
	try:
		if (ACK == 0 and final == "yes"):
			print "break from While with ACK and Yes"
			break

		pick = time_out[0]
		#print "Timer:: ", time_out
		timee = 3 - (time.time() - pick[1])
		while (timee < 0):
			#print "Timee"
			test_resend(str(pick[0]))
			time_out.pop(0)	
			pick = time_out[0]
			timee = 3 - (time.time() - pick[1])
			#print "Timee"

		#print "Timeout is set to : ","[",pick[0],"]", (timee)
		serverSocket.settimeout(timee)
		ACK, addr = serverSocket.recvfrom(1018)
		if (final == "yes"):
			print "ACK = ", ACK
		serverSocket.settimeout(None)
		time_out.pop(0)
		#print "Timer:: ", time_out
		
		
		ACK = get_seq_number_as_int(ACK,"_")
		#print "Got this ACK: ", ACK
		seq_chk[ACK] = str(ACK)
		#print "seq_chk : ", seq_chk
		if (ACK >= 0 and ACK != (size_of_array - 1) ):
			#print "ACK = ", ACK, " : ",len(file_content) 
			if (nxt <= (size_of_array -1) and final != "yes"):
				string = str(nxt) + division_key + content_array[nxt]
				#print "sending..", len(string)
				serverSocket.sendto(string , addr)
				time_out.append([nxt,time.time()])

				len_check(seq_chk,nxt)
				seq_chk[nxt]  = "XXX"

				last = nxt
				nxt = nxt + 1
			else:
				if (seq_chk.count("XXX") > 0):
					print "Resending XXX ",seq_chk.index("XXX")
					test_resend(str(seq_chk.index("XXX")))
					
					#time_out.pop(0)
				else:
					print "final loop with END"
					string = "0" + division_key + "end"
					serverSocket.sendto(string , addr)
					final = "yes"
					time_out.append([pick[0]+1,time.time()])

		else:
			print "exit from while with the new conditon"
			if (seq_chk.count("XXX") == 0  ):
				print "break.."
				#break
				continue
			else:
				print "continue"
				continue
	except timeout:
		#print "Sending (( ", pick[0]
		test_resend(str(pick[0]))
		time_out.pop(0)
		continue

#print "seq_chk : ", seq_chk
print "the timer has: ", time_out
print "Finished from while loop, File size", len(file_content)
#print last , " :: ", len(content_array[size_of_array -1]), " :: ", len(content_array[size_of_array -2])

serverSocket.sendto('0'+division_key+'uiowa' , addr)

serverSocket.close()