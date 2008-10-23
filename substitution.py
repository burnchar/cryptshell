#!/usr/bin/env python

import sys
import freqanalysis

class Substitution:

  def __init__(self, args):
    args = args.replace(' ', '')
    self.cipherText = args
    self.cipherLength = len(args)

  def mainLoop(self):
    while 1:
      command=raw_input('What would you like to do? (Press "show" to show your options) >').lstrip()
      if command.lower().startswith('show'):
        self.showOptions()
      elif command.lower().startswith('print'):
        self.printFrequency()
      elif command.strip().lower() == "exit":
        print "leaving substitution..."
        break
      else:
        print "Error: command not recognized. Press s to show your options."

  def showOptions(self):
    print 'print'
    print 'exit'
    print 'show'

  def getFreq(self, val):
    freq = float(self.cipherText.count(val))
    return (freq/self.cipherLength)

  def getFreqTable(self):
    letterList = []
    for i in self.cipherText:
      if letterList.count(i) == 0:
        letterList.append(i)

    cipherFreqTable = {}
    for c in letterList:
      freq = self.getFreq(c)
      cipherFreqTable[c] = freq
    return cipherFreqTable

  def getFrequency(self):
    cipherFreqTable = self.getFreqTable()
    myFreq = freqanalysis.xfrequencyTable(cipherFreqTable)

  def printFrequency(self):
    cipherFreqTable = self.getFreqTable()
    myFreq = freqanalysis.xfrequencyTable(cipherFreqTable)
    myFreq.printEnglishvFreq()

if __name__ == "__main__":

  stringToCrypt = sys.argv[1]
  print 'Cipher Text is: ' + str(stringToCrypt)

  myAnalysis = Substitution(stringToCrypt)
  myAnalysis.getFrequency()


