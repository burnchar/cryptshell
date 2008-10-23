#!/usr/bin/python

import numpy 
import matplotlib.pyplot as plt

#hard coded frequencies of languages
EnglishFreqTable = {
  'a': .08167,
  'b': .01492,
  'c': .02782,
  'd': .04253,  
  'e': .12702,
  'f': .02228,
  'g': .02015,
  'h': .06094,
  'i': .06966,
  'j': .00153,
  'k': .00772,
  'l': .04025,
  'm': .02406,
  'n': .06749,
  'o': .07507,
  'p': .01929,
  'q': .00095,
  'r': .05987,
  's': .06327,
  't': .09056,
  'u': .02758,
  'v': .00978,
  'w': .02360,
  'x': .00150,
  'y': .01974,
  'z': .00074 }

#more languages should be added for further analysis

def max(a, b):
  if a > b:
    return a
  else:
    return b

def dictToTupleList(dictionary):
  mlist = []
  for i in dictionary.keys():
    mlist.append((i, dictionary[i]))
  return mlist

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height,("%.2f" % height),
                ha='center', va='bottom')

def listequalizer(list1, list2):
  for i in list1:
    if i[0] not in [a for a,b in list2]: 
      list2.append((i[0],0))
  for i in list2:
    if i[0] not in [a for a,b in list1]:
      list1.append((i[0],0))
  return len(list1) 

class xfrequencyTable():
  def __init__(self, freqdict, width=.35):
    #this may be used for comparing frequencies to languages
    self.letterdict = freqdict
    self.N = max(len(freqdict), len(EnglishFreqTable))
    self.width = width
    #todo pad values so they're the same width

  def replaceAll(self):
    englishFreq = dictToTupleList(EnglishFreqTable)
    cipherFreq = dictToTupleList(self.letterdict)
    print 'blah blah blah'

  def printEnglishvFreq(self, sortmethod='letter'):
    englishFreq = dictToTupleList(EnglishFreqTable)
    cipherFreq = dictToTupleList(self.letterdict)
    #pad the lists so they contain the same elements
    self.N = listequalizer(englishFreq, cipherFreq)
    englishFreq.sort()
    cipherFreq.sort()
    ind = numpy.arange(self.N)
    plt.subplot(111)
    rects1 = plt.bar(ind,[b for a, b in englishFreq], self.width, color='r')
    rects2 = plt.bar(ind+self.width,[b for a,b in cipherFreq], self.width, color='y')
    #add some labels for our line graph
    plt.ylabel("Frequency")
    plt.title("Frequency of English vs Ciphertext")
    #this is the labeling for the bottom - may need fixing
    plt.xticks(ind+self.width, [a for a,b in englishFreq] ) 
    plt.legend( (rects1[0], rects2[0]), ("English", "Cipher") )
    #apply the labels
    autolabel(rects1)
    autolabel(rects2)
    #set this soon
    xmin, xmax, ymin, ymax = plt.axis()
    plt.ylim(0, ymax + .03)  
    #I would like to make these bigger, but they must be set in the backend
    #therefore, for the sake of being portable, I'll just leave it for now
    #they can always be resized
    plt.show()   

if __name__ == "__main__":
  #this is just a stupid table here for demonstration
  cipherFreqTable = {
    'r': .08167,
    'b': .01492,
    'l': .02782,
    'd': .24253,  
    'f': .12228,
    'g': .02015,
    'h': .06094,
    'i': .06966,
    'j': .00153,
    'k': .10772,
    'c': .04025,
    'm': .02406,
    'n': .06749,
    'q': .07507,
    'o': .00095,
    'a': .05987,
    's': .06327,
    't': .09056,
    'u': .02758,
    'v': .00978,
    'w': .02360,
    'z': .00074,
    'A': 0,
    'B': 0,
    'C': 0,
    'E': .1 }

  m = xfrequencyTable(cipherFreqTable)
  m.printEnglishvFreq()  
