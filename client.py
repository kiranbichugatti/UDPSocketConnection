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

sentence = "Hello, From Client"
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(sentence, (serverName, serverPort))


clientSocket.close()
