#!/usr/bin/env python

import pygame
import sys
import time
from tpllink import *

class MorseGenerator():

    def __init__(self):

        self.CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
                'D': '-..',    'E': '.',      'F': '..-.',
                'G': '--.',    'H': '....',   'I': '..',
                'J': '.---',   'K': '-.-',    'L': '.-..',
                'M': '--',     'N': '-.',     'O': '---',
                'P': '.--.',   'Q': '--.-',   'R': '.-.',
                'S': '...',    'T': '-',      'U': '..-',
                'V': '...-',   'W': '.--',    'X': '-..-',
                'Y': '-.--',   'Z': '--..',
                
                '0': '-----',  '1': '.----',  '2': '..---',
                '3': '...--',  '4': '....-',  '5': '.....',
                '6': '-....',  '7': '--...',  '8': '---..',
                '9': '----.' 
                }
            
        self.ONE_UNIT = 0.5
        self.THREE_UNITS = 3 * self.ONE_UNIT
        self.SEVEN_UNITS = 5 * self.ONE_UNIT
        self.PATH = 'morse_sound_files/'
        self.mList = []

    def dash(self, tpl):
        print "-",
        tpl.iotOn()
        time.sleep(self.THREE_UNITS)
        tpl.iotOff()
        time.sleep(2*self.ONE_UNIT)

    def dot(self, tpl):
        print ".",
        tpl.iotOn()
        #time.sleep(self.ONE_UNIT)
        tpl.iotOff()
        #time.sleep(self.ONE_UNIT)

    def pause(self, tpl):
        print " ",
        tpl.iotOff()
        time.sleep(self.SEVEN_UNITS)


    def getMorse(self, msg="SOS"):
        tpl = tpllink()    
        try:
            for char in msg:
                if char == ' ':
                    print '  '*7,
                    # time.sleep(self.SEVEN_UNITS)
                else:
                    # print self.CODE[char.upper()] 
                    self.getAudio(char)
                    for sign in self.CODE[char.upper()]:
                        if sign == '.':
                            self.dot(tpl)
                        elif sign == '-':
                            self.dash(tpl)
                        else:
                            self.pause(tpl)
                    # time.sleep(self.THREE_UNITS)
        except Exception as e:
            print 'Error the charcter ' + char + ' cannot be translated to Morse Code'
            print e.message
        
    def getAudio(self, char):
        pygame.init()
        pygame.mixer.music.load(self.PATH + char.upper() + '_morse_code.ogg')
        pygame.mixer.music.play()
        return

myMorse = MorseGenerator()
myMorse.getMorse(raw_input('MESSAGE: '))


