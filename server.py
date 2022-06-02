#!/usr/bin/python3

#-*- coding:UTF-8 -*-

import socket, time, subprocess

def parser(stringclient):
	return stringclient.upper()

host="127.0.0.1"
port=12555
subprocess.Popen("fuser -k "+str(port)+"/tcp", shell=True)
print("Free back door")
time.sleep(3)
print("Server started")

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

while(True):
	c, addr=s.accept()
	print("Connection established with "+str(addr))
	inputmessage=c.recv(1024).decode()
	print("Message from client: "+inputmessage)
	outputmessage=parser(inputmessage)
	c.send(outputmessage.encode())
	print("Message from server: "+outputmessage)
	c.close
	print("Connection interrupted with "+str(addr))
