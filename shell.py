#!/usr/bin/env python

import readline, sys, copy, getopt, collections, re
import cryptanal
import rotor, vigenere, substitution, freqanalysis


"""
The shell class is the front end for cryptanal 
and includes interfaces to the entire backend 
"""
class shell:
  def __init__(self, cryptobj=None):
    print"""
WWW         WW eEeEeEeE LL        CCCCC    OOOO    MMMM    MMMM  eEeEeEeE
 WW         W  EE       LL       Cc      OOO  OOO  MM MM  M  MM  EE
  WW       WW  EeEeE    LL      CC       OO    OO  MM  MMM   MM  EeEeE
  WWw WW  WW   EE       LL       Cc      OOO  OOO  MM        MM  EE
   WWW  WWW    eEeEeEeE LlLlLlL   CCCCC    OOOO    MM        MM  eEeEeEeE
  
                             TO CRYPTO-SHELL
  (Useful for deciphering what little Susie is writing to little Billy)
"""

    #if this is none there should be a way to open a new one
    self.rootcrypto = cryptobj
    self.currcrypto = copy.deepcopy(cryptobj)

    #setup the tab completion information here
    self.commands = ["help", "print", "save", "revert", "open", "sub", "trans", "quit", "enigma", "vigenere", "substitution"]
    readline.set_completer(self.completer)
    readline.parse_and_bind("tab: complete")
    
  ############################################
  #Below is the main front-end interface
  #including support for gnu readline 
  #and print functions
  ############################################

  #completer funtion for tab complete
  def completer(self, word, index):
    matches = [c for c in self.commands if c.startswith(word)]
    try:
      return matches[index] + " "
    except IndexError:
      pass

  #this is the main event loop
  def mainloop(self):
    while 1:
      command=raw_input('> ').lstrip()
      if command.lower().startswith('help'):
        self.help(command[4:].lstrip())
      if command.lower().startswith('save'):
        self.save(command[4:].lstrip())
      elif command.lower().startswith('revert'):
        self.Revert(command[6:].strip())
      elif command.lower().startswith('print'):
        self.Print(command[5:].strip())
      elif command.lower().startswith('substitution'):
        args = command[12:].split()
        self.substitution(args)
      elif command.lower().startswith('sub'):
        args = command[3:].split()
        self.sub(args)
      elif command.lower().startswith('enigma'):
        args = command[6:].split()
        self.enigma(args)
      elif command.lower().startswith('vigenere'):
        args = command[8:].split()
        self.vigenere(args)
      elif command.lower().startswith('trans'):
        args = command[5:].split()
        self.transpose(args)
      elif command.strip().lower() == "quit" or command.strip().lower() == "exit":
        print "come again soon...  "
        sys.exit()
      else:
        print "Error: command not recognized: type 'help' for usage"
     
  #this is the main help function 
  def help(self, args):
    print "HELP"

  #revert back to the original
  def Revert(self, args):
    self.currcrypto = copy.deepcopy(self.rootcrypto)

  #The print function will print the cipher in various ways
  def Print(self, args):
    printhelp = 0
    if args.strip() == "current":
      self.currcrypto.printcrypt()
    elif args.strip() == "orig":
      self.rootcrypto.printcrypt()
    elif args.strip() == "freq":
      self.currcrypto.printsorteddict()
    elif args.strip() == "graph":
      self.PrintGraph()
    elif args.strip() == "help":
      self.PrintUsage()
    else:
      self.PrintUsage()

  def PrintGraph(self):
    #this for the printing graphs
    #right now, it is overly-siplified
    #the only way to print is the cipher vs english, grouped by letter
    #but more options will be added later, so this functions should stay existing
    try:
      import freqanalysis, os
      newpid = os.fork()
      #fork a new process so the graph doesn't tie up the shell
      if newpid == 0:
        m = freqanalysis.xfrequencyTable(self.currcrypto.getfreq())
        m.printEnglishvFreq() 
        sys.exit()
    except SystemExit:
      print "graph exited" 
      sys.exit()
    except:
      print """Error: check that numpy and matplotlib are installed
    you also probably can't use windows because there is a fork"""
      print sys.exc_info()[0]

  def PrintUsage(self):
    print """Usage: print [current | orig | freq]

  current		prints current crypto decoding
  orig			prints original ciphertext
  freq			prints a simple frequency analyses count
  graph 		prints various graphs - must have matplotlib installed

  help			print this screen
  """
 
  ############################################
  #Below are the Substitution an Transpose interfaces
  #which are common to many cryptographic systems
  ###########################################

  def sub(self, args): 
    #set default argumetns
    subhelp = False
    startrange = 0
    endrange = None
    jumpval = 1
    try:
      fromstr = args[0]
      tostr = args[1]
    #get arguments
      options, arguments = getopt.getopt(args[2:], "s:e:j:", ["startrange=", "endrange=", "jumpval="])
      for o, a in options:
        if o in ("-s", "--startrange"):
          startrange = int(a)
        elif o in ("-e", "--endrange"):
          endrange = int(a)
        elif o in ("-j", "--jumpval"):
          jumpval = int(a)
        else:
          subhelp = True
          break
      if subhelp == True:
        self.subUsage()
      else:
        self.currcrypto.substitute(fromstr, tostr, startrange, endrange, jumpval)
    except:
      self.subUsage()
      return

  def subUsage(self):
    print """Usage: sub fromstring tostring [-s | --startrange startrange] [-e | --endrange endrange] [-j | --jumpval jumpvalue]

  fromstring		original character to be replaced
  tostring		character to replace fromstring
  -s,--startrange	index (starting with 0) in which to start replacing letters
  -e,--endrange		index in which to stop replacing letters
  -j,--jumpvalue	allows operation on series of values that are not necessarily next to eachother"""

  def transpose(self, args): 
    #set default arguments
    transHelp = False
    shiftl = 1
    shiftr = 0
    srange = 0
    endrange = len(self.currcrypto.letterlist) - 1
    shifterrorcheck = 0
    try:
      options, arguments = getopt.getopt(args, "l:r:s:e:j:", ["lshift=", "rshift=", "srange=", "endrange=", "help"])
      for o, a in options:
        if o in ("-l", "--lshift"):
          shiftl = int(a)
          #this is only an error if right shift is also set
          shifterrorcheck += 1
        elif o in ("-r", "--rshift"):
          shiftr = int(a)
          #only an error if shiftl is also set
          shifterrorcheck += 1
        elif o in ("-s", "--srange"):
          srange = int(a)
        elif o in ("-e", "--endrange"):
          endrange = int(a)
        elif o in ("--help"):
          transHelp = True
        else:
          transHelp = True
        if transHelp == True:
          break
      if shifterrorcheck >= 2 or arguments:
        transHelp = True
      if transHelp == True:
        self.transHelp()
      else:
        if shiftr != 0:
          shiftl = len(self.currcrypto.letterlist) - shiftr
        self.currcrypto.transpose(shiftl, srange, endrange)
    except:
      self.transHelp()
      return

  def transHelp(self):
    print """Usage: trans [[-l --lshift value | -r --rshift value] [-s | --srange] [-e | --endrange] | --help]

  -l, --lshift		number of places to shift left
  -r, --rshift		number of places to shift right
  -s, --srange		where to start transposing
  -e, --endrange	where to end transposing
  --help		print this message and exit
  """
 
  ###########################################
  #functions for saving, opening and reverting
  #your analysis session
  ###########################################
  
  #save a new version of what you've done
  def save(self, name):
    if name is "":
      name = "out.txt"
    f=open(name, 'w')
    f.write(self.currcrypto.getcrypt())
    f.close()
    print "Saved in " + name

  #open a previous version
  def open(self, name):
    print "OPENING"
  
  ###########################################
  #front ends for specific ciphers      
  ###########################################

  #Substitution Cipher
  def substitution(self, args):
    cryptToSend = self.currcrypto.getcrypt()
    cryptToSend = cryptToSend.replace(' ', '')  # deleting all white space
#    cryptToSend = cryptToSend.lower() # make all letters lower-case for comparison with english letter frequencies
    sub = substitution.Substitution(cryptToSend)
    cipherFreqTable = sub.getFreqTable()
    freq = freqanalysis.xfrequencyTable(cipherFreqTable)
    myNewText = freq.replaceAll()
    sub.mainLoop()
#    freqComparison = sub.getFrequency()

  #The Vigenere cipher
  def vigenere(self, args):
    usageProblem = False	
    try:
      options, arguments = getopt.getopt(args, "k:edh", ["key=", "encrypt", "decrypt", "help"])
    except getopt.GetoptError, err:
      usageProblem = True    
    if usageProblem == False:   
      key = "default"   
      encrypt = 0 
      decrypt = 0 
      doVigenere = False  
      help = 0  
      for o, a in options:
	if o in ("-e", "--encrypt"):
	  doVigenere = True	
	  encrypt = 1      
	elif o in ("-d", "--decrypt"):
	  doVigenere = True
	  decrypt = 1	
	elif o in ("-k", "--key"):
          key = a	
        elif o in ("-h", "--help"):
          help = 1	
      if help == 1:
        vigUsage()
      if doVigenere is True:  
	vig = vigenere.Vigenere(self.currcrypto.getcrypt().strip(), key)      
	if encrypt == 1 and decrypt == 1:
	  #usage problem, -d and -e cannot be used at the same time
          vigUsage()
	elif encrypt == 1:
	  res = vig.cypher()
	  self.currcrypto.setcrypt(res)		 
	elif decrypt == 1:
	  res = vig.decypher()
	  self.currcrypto.setcrypt(res)	
      else:
        #at least -d or -e have to be used
        vigUsage()
  
  def vigUsage():
    print """Usage: vigenere [-e | --encrypt] | [-d | --decrypt] [-h | --help] [-k | --key cipherKey] "
    -e, --encrypt                Encrypt input.  Can not be used with the -d switch.  
    -d, --decrypt                Decrypt input.  Can not be used with the -e switch.  
    -k, --key                    Set the key used to encrypt or decrypt an input (string). If not used, key="default"  
    -h, --help                   Print this screen.  
    """
	
  #The enigma cipher	
  def enigma(self, args): 
    # Default values needed for syntax checking and -h options. 
    encipher = 0
    decipher = 0
    enigmaU = False
    # The next section parses the arguments "args" grabed from the command line and passed down from the shell.  
    try:
      options, arguments = getopt.getopt(args, "r:k:eduh", ["key=", "rotors=", "encrypt", "decrypt", "unknown", "help"])
    except getopt.GetoptError, err:
      # this exception is executed if there is an option passed that is not defined.  Normally this would have an exit,
      # or there would be an exit in the usage and you would call the usage here.  
      enigmaU = True
    # Since Python does not have a goto command and I don't want to exit the shell I set a variable that makes most of
    # the code get skipped if there is a usage problem.  
    if enigmaU is not True:
      # Default settings for the cipher program.  
      keys = "default"
      kVar = False
      rotors = 3
      rVar = False
      encryption = True
      unknown = False
      # conditions and variables that are set depending on the options passed
      for o, a in options:
        if o in ("-d", "--decrypt"):
          encryption = False
          decipher = 1
        elif o in ("-e", "--encrypt"):
          encryption = True
          encipher = 1
        elif o in ("-h", "--help"):
          enigmaU = True
        elif o in ("-k", "--key"):
          keys = a
          kVar = True
        elif o in ("-r", "--rotors"):
          rotors = a
          rVar = True
        elif o in ("-u", "--unknown"):
          encryption = False
          decipher = 1
          unknown = True
          if rVar is True and kVar is True:
            enigmaU = True
        elif enigmaU is True:
          # this conditional breaks out of the for loop if the help options is called.  
          break
        else:
          # this conditional sets the usage flag and breaks out of the for loop if there is an unhandled condtion
          # in the command line.  
          enigmaU = True
          break
      if encipher and decipher:
        # this conditional flags if the -e and -d are both called.  They are mutually exclusive.  
        print "The -e and -d/u are mutually exclusive.  "
        enigmaU = True
      try:
        rotors = int(rotors)
      except:
        enigmaU = True
        print "Rotors must be an int.  "
      if unknown is True:
        # print "unknown switch set.  "
        if rVar is True:
          enigmaU = True
          print "The key (-k) must be specified, and the rotor (-r) must not be specified.  "

    if enigmaU is True:
      enigmaUsage()
    else:
      rt = rotor.newrotor(keys, rotors)
      if encryption == True:
        self.currcrypto.setcrypt(rt.encrypt(self.currcrypto.getcrypt()))
        print "Key and rotors are set to: " + keys + ", " + str(rotors)
      else:
        if unknown == False:
          self.currcrypto.setcrypt(rt.decrypt(self.currcrypto.getcrypt()))
          print "Key and rotors are set to: " + keys + ", " + str(rotors)
        else:
          # This loop will need to be run when searching for a decryptions configuration
          # loop through more than one word in a string.  
          percent = 0.0
          decriptIterator = 0
          while percent < 50 and decriptIterator < 20:
            percent = 0.0
            percentNum = 0
            percentDen = 0
            rt = rotor.newrotor(keys, decriptIterator)
            # self.currcrypto.setcrypt(rt.decrypt(self.currcrypto.getcrypt()))
            for word in rt.decrypt(self.currcrypto.getcrypt()).split():
              if dictionary([word.lower().rstrip('.')]):
                percentNum += 1
              percentDen += 1
            percent = (float(percentNum)/float(percentDen))*100
            if percent > 50:
              self.currcrypto.setcrypt(rt.decrypt(self.currcrypto.getcrypt()))
              print "Key and rotors are set to: " + keys + ", " + str(decriptIterator)
            decriptIterator += 1

def dictionary(words):
  model = collections.defaultdict(lambda: 1)
  ALLWORDS = re.findall('[a-z]+', file('/etc/dictionaries-common/words').read().lower())
  for f in ALLWORDS:
    model[f] += 1
  return set(w for w in words if w in model)

def enigmaUsage():
  print """Usage: enigma [-e | --encrypt] | [-d | --decrypt] [-u | --unknown] [-h | --help] [-k | --key cipherKey] [-r | --rotor cipherRotorNumber] "
  -e, --encrypt                Encrypt input.  Can not be used with the -d switch.  
  -d, --decrypt                Decrypt input.  Can not be used with the -e switch.  
  -u, --unknown                Unknown rotor number for the given encrypted input.  
                               Note this option only is used for decryption it has 
                               no effect if the -e or --encrypt switchs are set.  
  -k, --key                    Set the key used to encrypt or decrypt an input (string).  
  -r, --rotors                 Set the number of rotors used to encrypt or decrypt an input (int).  
  -h, --help                   Print this screen.  
"""
                          

if __name__ == '__main__':

  #this needs to be improved by quality assurance
  letterlist = open(sys.argv[1]).read()
  rootphrase = cryptanal.CryptAnal(letterlist) 
 
  thisshell = shell(rootphrase)
  thisshell.mainloop()
