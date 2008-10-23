#!/usr/bin/env python

"""
This program is a basic cryptanalysis tool
useful for finally finding out what little Susie is writing to Billy
or what Caeser is writing to the Romans

This is meant to be a parent class. Write subclasses to this interface
for added functionality
"""

import sys

class CryptAnal():
  def __init__(self, wordlist):
    self.letterlist = wordlist 
    self.totalnum = len(wordlist)

  def __calcfreq__(self, letters):
    #calculate the frequencies  
    dictionary = {}
    for i in letters:
      if i in dictionary:
        dictionary[i] += 1
      else:
        dictionary[i] = 1
    #freqlist stores an unsorted  list of the frequencies
    self.freqlist = [(a,b) for b,a in dictionary.items()]

  def substitute(self, fromstr, tostr, startrange=0, endrange=None, jumpval=1):
    #setting the endrange default value to the strlen
    if endrange == None:
      endrange = int(self.totalnum) - 1
    for i in range (startrange, endrange, jumpval):
      if self.letterlist[i] == fromstr:
        self.letterlist = self.letterlist[:i] + tostr + self.letterlist[i+1:]

  #this shifts letters. 
  #eg 'abcdefg' shifted by defaults will give 'bcdefga'    
  def transpose(self, shiftl=1, startrange=0, endrange=None):
    #set default endrange
    if endrange == None:
      endrange = int(len(self.letterlist)-1)
    #make a list so we can swap the elements around
    templist = []
    for i in self.letterlist:
      templist.append(i)
    tempvar = self.letterlist[startrange + shiftl - 1]
    for i in range(startrange, endrange):
      templist[i] = self.letterlist[(i+shiftl)%(endrange+1)]
    templist[endrange] = tempvar
    self.letterlist = "".join(templist)

  #this prints the letters in the list
  def printcrypt(self):
    print self.letterlist

  #print a sorted count of all letters 
  #this needs work - should be able to sort on multiple items, have different indices, etc
  #def printsorteddict(self, letterlist=None, startrange=0, endrange=None, jumpval=1):
  def printsorteddict(self, letterlist=None):
    #get default letter list
    if letterlist == None:
      letterlist = self.letterlist
    self.__calcfreq__(letterlist)
    self.freqlist.sort()
    self.freqlist.reverse()
    print "Frequency\tLetter\t\tAscii\t\tRatio"
    print "--------------------------------"
    for i in self.freqlist:
      if i[1] != '\n':
        print i[0], "\t\t", str(i[1]),"\t\t",ord(i[1]),"\t\t", float(i[0])/self.totalnum
      else:
        print i[0], "\t\t", '\\n',"\t",ord(i[1]),"\t", i[0]/self.totalnum

  #this sets the letters in the list (this is handy if you
  #do encryption not using the substitute, or transpose
  #functions to do an encryption/manipulation.  
  def setcrypt(self, cryptlist):
    self.letterlist = cryptlist 
    self.totalnum = len(cryptlist)

  #this returns the letters in the list (this is handy if you
  #want to get the letters in the current object, but don't 
  #want to print them.  Again a function most useful if you
  #don't intend to use the built in encryption tools.  
  def getcrypt(self):
    return self.letterlist

  def getfreq(self):
    self.__calcfreq__(self.letterlist)
    dict = {}
    for i in self.freqlist:
      dict[i[1]] = float(i[0])/self.totalnum
    return dict
