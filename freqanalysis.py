#!/usr/bin/python

import numpy
try:
  import matplotlib.pyplot as plt
except:
  print "Warning: matplotlib.pyplot is not available."


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

# Tables of frequency for non-English languages.
# Each of these has more characters available than the standard English 26,
# but some terminals cannot display them, and most (but not all) are fairly infrequent.

FrenchFreqTable = {
  'a': 	.07636,
  'b': 	.00901,
  'c': 	.03260,
  'd': 	.03669,
  'e': 	.14715,
  'f': 	.01066,
  'g': 	.00866,
  'h': 	.00737,
  'i': 	.07529,
  'j': 	.00545,
  'k': 	.00049,
  'l': 	.05456,
  'm': 	.02968,
  'n': 	.07095,
  'o': 	.05378,
  'p': 	.03021,
  'q': 	.01362,
  'r': 	.06553,
  's': 	.07948,
  't': 	.07244,
  'u': 	.06311,
  'v': 	.01628,
  'w': 	.00114,
  'x': 	.00387,
  'y': 	.00308,
  'z': 	.00136,
}

SpanishFreqTable = {
  'a': 	.12530,
  'b': 	.01420,
  'c': 	.04680,
  'd': 	.05860,
  'e': 	.13680,
  'f': 	.00690,
  'g': 	.01010,
  'h': 	.00700,
  'i': 	.06250,
  'j': 	.00440,
  'k': 	.00000,
  'l': 	.04970,
  'm': 	.03150,
  'n': 	.06710,
  'o': 	.08680,
  'p': 	.02510,
  'q': 	.00880,
  'r': 	.06870,
  's': 	.07980,
  't': 	.04630,
  'u': 	.03930,
  'v': 	.00900,
  'w': 	.00020,
  'x': 	.00220,
  'y': 	.00900,
  'z': 	.00520
}

GermanFreqTable = {
  'a': 	.06510,
  'b': 	.01890,
  'c': 	.03060,
  'd': 	.05080,
  'e': 	.17400,
  'f': 	.01660,
  'g': 	.03010,
  'h': 	.04760,
  'i': 	.07550,
  'j': 	.00270,
  'k': 	.01210,
  'l': 	.03440,
  'm': 	.02530,
  'n': 	.09780,
  'o': 	.02510,
  'p': 	.00790,
  'q': 	.00020,
  'r': 	.07000,
  's': 	.07270,
  't': 	.06150,
  'u': 	.04350,
  'v': 	.00670,
  'w': 	.01890,
  'x': 	.00030,
  'y': 	.00040,
  'z': 	.01130
 }

ItalianFreqTable = {
  'a': 	.11740,
  'b': 	.00920,
  'c': 	.04500,
  'd': 	.03730,
  'e': 	.11790,
  'f': 	.00950,
  'g': 	.01640,
  'h': 	.01540,
  'i': 	.11280,
  'j': 	.00000,
  'k': 	.00000,
  'l': 	.06510,
  'm': 	.02510,
  'n': 	.06880,
  'o': 	.09830,
  'p': 	.03050,
  'q': 	.00510,
  'r': 	.06370,
  's': 	.04980,
  't': 	.05620,
  'u': 	.03010,
  'v': 	.02100,
  'w': 	.00000,
  'x': 	.00000,
  'y': 	.00000,
  'z': 	.00490
}

TurkishFreqTable = {
  'a': 	.11680,
  'b': 	.02950,
  'c': 	.00970,
  'd': 	.04870,
  'e': 	.09010,
  'f': 	.00440,
  'g': 	.01340,
  'h': 	.01140,
  'i': 	.08270,
  'j': 	.00010,
  'k': 	.04710,
  'l': 	.05750,
  'm': 	.03740,
  'n': 	.07230,
  'o': 	.02450,
  'p': 	.00790,
  'q': 	.00000,
  'r': 	.06950,
  's': 	.02950,
  't': 	.03090,
  'u': 	.03430,
  'v': 	.00980,
  'w': 	.00000,
  'x': 	.00000,
  'y': 	.03370,
  'z': 	.01500
}

SwedishFreqTable = {
  'a': 	.09300,
  'b': 	.01300,
  'c': 	.01300,
  'd': 	.04500,
  'e': 	.09900,
  'f': 	.02000,
  'g': 	.03300,
  'h': 	.02100,
  'i': 	.05100,
  'j': 	.00700,
  'k': 	.03200,
  'l': 	.05200,
  'm': 	.03500,
  'n': 	.08800,
  'o': 	.04100,
  'p': 	.01700,
  'q': 	.00007,
  'r': 	.08300,
  's': 	.06300,
  't': 	.08700,
  'u': 	.01800,
  'v': 	.02400,
  'w': 	.00030,
  'x': 	.00100,
  'y': 	.00600,
  'z': 	.00020
}

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
    try:
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
    except NameError:
      print "Warning: matplotlib.pyplot is not available."

if __name__ == "__main__":
  import cryptanal, pickle, sys
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

  cipherFreqTable = pickle.loads(sys.argv[1])

  m = xfrequencyTable(cipherFreqTable)
  m.printEnglishvFreq()
