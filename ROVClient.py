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
    reply = s.recv(16)
    s.send("EXIT")
    s.close()
    return reply

def transmit(message):
    s = setupSocket()
    response = sendReceive(s, message)
    return response
