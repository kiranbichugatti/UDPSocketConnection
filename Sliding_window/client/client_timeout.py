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
serverPort = 14010
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
def len_check(arr,num):
	while len(arr) < (num + 1):
		arr.append("asnobi")
def get_str_arr(arr):
	msg = ""
	for i in range (len(arr)):
		if(arr[i] != "asnobi"):
			msg = msg + arr[i]
	return msg

def test_recv():
	#print "inside recive func"
	clientSocket.settimeout(None)
	reply, addr = clientSocket.recvfrom(1020)
	#clientSocket.settimeout(4)
	seq = get_seq_number_as_int(reply, division_key)
	len_check(reciving_MSG,seq+1)

	len_check(seq_chk, seq)
	seq_chk[seq] = seq
	
	reply = get_String(reply,division_key)
	#print "reciving_MSG,befor ", print_arrr(reciving_MSG)
	reciving_MSG[seq] = reply
	if (recived.count(str(seq))==0):
		recived.insert(0,seq)

	#print "recived ==", recived
	#print "Done: ", seq
	#print "Done: ", reply[:5]
	#print "reciving_MSG,after ", print_arrr(reciving_MSG)

def print_arrr(arr):
	q = ""
	for i in range(len(arr)):
		if (len(arr[i]) > 0):
			q = q +" , "+ arr[i][:8]
		else:
			q = q +" , "

	return q


sentence = "Hello, From Client"
clientSocket = socket(AF_INET, SOCK_DGRAM)
sentence = "GET " + file_requested + " HTTP/1.1%s" % (newline)


clientSocket.sendto(sentence, (serverName, serverPort))
#clientSocket.settimeout(4)

MSG = ""
reply= ""
dirr = os.path.dirname(file_requested)
output_file = open(file_requested, 'w')

recived = []
seq_chk = []
reciving_MSG = []
startTime = time.time()

###############
for i in range (windowSize):
     try:
	reply, addr = clientSocket.recvfrom(1020)
	#if (len(reply)<10 ):
		#print "I Got reply: ", reply
	seq = get_seq_number_as_int(reply, division_key)
	recived.append(seq)
	reply = get_String(reply,division_key)
	len_check(reciving_MSG,seq+1)

	#print "recived this , ", reply[:8]
	
	#print "befor , ", print_arrr(reciving_MSG)
	reciving_MSG[seq] = reply
	#print "after , ",print_arrr(reciving_MSG)

	len_check(seq_chk, seq)
	seq_chk[seq] = seq

	MSG = MSG + reply
     except timeout:
	test_recv()
	continue

reply = MSG
T = True
a = True

print "Finished from FOR loop"
while len(recived) != 0:
	try:


		#print "recived is ,", recived
		
		clientSocket.sendto(str(recived[0])+"_"+str(len(reply)), (serverName, serverPort))
		recived.pop(0)

		if (reply != "end"):


			#print "recived this , ", reply[:8]
			#print "befor , ", print_arrr(reciving_MSG)
			len_check(reciving_MSG,seq+1)
			reciving_MSG[seq] = reply
			#print "After , ", print_arrr(reciving_MSG)

			#if (len(reply)<10 ):
			#	print "reply: ", reply
			MSG = MSG + reply




			reply, addr = clientSocket.recvfrom(1020)
			seq = get_seq_number_as_int(reply, division_key) #f
			recived.append(seq)

			len_check(seq_chk, seq)
			seq_chk[seq] = seq

			reply = get_String(reply,division_key)



	except timeout:
		test_recv()
		continue

#print "Finished from while loop", seq

#clientSocket.sendto("STOP!"+"_", (serverName, serverPort))

print "the code took: ", time.time() - startTime

tst = get_str_arr(reciving_MSG)
output_file.write(tst)

#print "Seq : ",seq_chk

output_file.close()
print "out...", reciving_MSG.count("asnobi") - 1
print "MSG : ",str(len(MSG))
#m = hashlib.md5()
#m.update(MSG)
#print m.hexdigest()
print "TST : ",str(len(tst))
#m.update(tst)
#print m.hexdigest()
clientSocket.close()
