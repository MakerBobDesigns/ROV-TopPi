#!/usr/bin/python

import socket

host = '10.66.66.2'
port = 2222


def setupSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def sendReceive(s, message):
    s.send(message)
    #s.send(str.encode(message))
    reply = s.recv(1024)
    #print("We have received a reply")
    #print("Send closing message.")
    s.send("EXIT")
    #s.send(str.encode("EXIT"))
    s.close()
    #reply = reply.decode('utf-8')
    return reply

def transmit(message):
    s = setupSocket()
    response = sendReceive(s, message)
    return response
