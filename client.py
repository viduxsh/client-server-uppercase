#!/usr/bin/python3

#-*- coding:UTF-8 -*-

from tkinter import *
from tkinter import messagebox
import socket

def sendfunction():
    data=""+object.get()+"#"+message.get()
    s.send(data.encode())
    reply=s.recv(1024).decode()
    robject, rmessage=reply.split("#")
    robjectbox=Label(face, text="object: "+robject)
    robjectbox.grid(row=4, column=0)
    rmessagebox=Label(face, text="message received: "+rmessage)
    rmessagebox.grid(row=5, column=0)

window=Tk()
window.geometry("600x200")
window.title("Loginbox")

object=StringVar()
message=StringVar()
robject=""
rmessage=""

s=socket.socket()
host="127.0.0.1"
port=12555
s.connect((host, port))

face=Frame(window)
face.pack()

objectbox=Label(face, text="object:")
objectbox.grid(row=0, column=0)
objectinputbox=Entry(face, width="20", bg="cyan", textvariable=object)
objectinputbox.grid(row=0, column=1)

messagebox=Label(face, text="message to send:")
messagebox.grid(row=1, column=0)
messageinputbox=Entry(face, width="20", bg="cyan", textvariable=message)
messageinputbox.grid(row=1, column=1)

login=Button(face, text="Send", command=sendfunction)
login.grid(row=3, column=1)

window.mainloop()
