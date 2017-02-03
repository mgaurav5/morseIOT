#!/usr/bin/env python

import time
import socket
import json

class tpllink:

    def __init__(self):
    	self.state = "off"
        self.ip = "192.168.0.XXX" #update your smartplug ip here
        self.port = 9999  # standard port
        self.socket = None
        self.recv_buffer = 2048
        self.commands = {'info'     : '{"system":{"get_sysinfo":{}}}', 'on': '{"system":{"set_relay_state":{"state":1}}}', 'off': '{"system":{"set_relay_state":{"state":0}}}'}



    def encrypt(self, string):
        key = 171
        result = "\0\0\0\0"
        for i in string:
            a = key ^ ord(i)
            key = a
            result += chr(a)
        return result

    def decrypt(self, string):
        key = 171
        result = ""
        for i in string:
            a = key ^ ord(i)
            key = ord(i)
            result += chr(a)
        return result

    def connectSocket(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# self.socket.settimeout(self.timeout)
		try:
		    self.socket.connect((self.ip, self.port))
		    self.connected = True
		except socket.error:
		    self.socket = None


    def closeSocket(self):
        if self.socket is not None:
            try:
                self.socket.close()
            finally:
                self.socket = None
        self.connected = False

    def getState(self):
        cmd = self.commands["info"]
        self.connectSocket()
        self.socket.send(self.encrypt(cmd))
        data = self.socket.recv(self.recv_buffer)
        self.closeSocket()
        recvd = self.decrypt(data[4:])
        state = json.loads(recvd)
        return state["system"]["get_sysinfo"]["relay_state"]  



    def iotOn(self):
        cmd = self.commands[self.state]
        if not self.getState():
            self.state = "on"
        cmd = self.commands[self.state]
        self.connectSocket()
        self.socket.send(self.encrypt(cmd))
        #data = self.socket.recv(self.recv_buffer)
        self.closeSocket()


    def iotOff(self):
        cmd = self.commands[self.state]
        if self.getState():
            self.state = "off"
        cmd = self.commands[self.state]
        self.connectSocket()
        self.socket.send(self.encrypt(cmd))
        #data = self.socket.recv(self.recv_buffer)
        self.closeSocket()
