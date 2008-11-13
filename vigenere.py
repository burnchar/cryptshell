#!/usr/bin/python

import sys

class Vigenere:
	
  def __init__(self, string, key):	   
    #list used to match letter of the alphabet and their index
    self.letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']    
    #create matrix
    #each row contains letters of the alphabet
    #each row is shifted by one letter
    self.m=[]
    for i in range(0,26):
      self.m.append([])
      for j in range(0,26):
        self.m[i].append(self.letters[(j+i)%26])
    	
    self.string = string
    self.key = key   
    #create a finalKey which is the encryption key repeated to fit the size of
    #the string to encrypt 
    self.finalKey = ""
    i=0
    for letter in self.string:
      if letter == " ":
        # white spaces stay 	   
        self.finalKey += " "
      else:
        self.finalKey += key[i]
        i+=1
      if i > len(key)-1:
        i=0 

  def cypher(self):		  
    #Encrypt string with the vigenere algorithm   
    toEncrypt = self.string[:]
    cryptedString = ""
    for i in range(0,len(toEncrypt)):
      # set the letter to crypt	
      letterToCrypt = toEncrypt[i]
      # set the corresponding key
      keyLetter = self.finalKey[i].lower()
  
      if letterToCrypt.isdigit():
	cryptedString += letterToCrypt      
      elif letterToCrypt == " ":
        cryptedString += letterToCrypt
      else:
        #letter crypted = the letter in the junction in the  matrix 
        #of the letter to encrypt and the corresponding key letter  
        #the letters list helps to match a letter and its index
	if letterToCrypt.isupper():
	  #if letter is upper, find solution zith lower letter then cast in big letter	
	  letterToCrypt = letterToCrypt.lower()	
          cryptedString += self.m[self.letters.index(letterToCrypt)][self.letters.index(keyLetter)].upper()
	else:
	  cryptedString += self.m[self.letters.index(letterToCrypt)][self.letters.index(keyLetter)]
    	
    return  cryptedString	

  def decypher(self): 	     	  
    # decode the encrypted string
    cryptedString = self.string[:] 
    decodedString=""
    for i in range(0,len(cryptedString)):
      # set the letter to decode
      letterToDecode = cryptedString[i]
      # set the corresponding key
      keyLetter = self.finalKey[i].lower()

      if letterToDecode.isdigit():   
	decodedString += letterToDecode      
      elif letterToDecode == " ":
        decodedString += letterToDecode
      else:
        #select column of keyletter	  
        col = self.letters.index(keyLetter)
        #find row where letter to decode is
        for i in range(0,25):
          if self.m[i][col] == letterToDecode.lower():    
	    #letter decoded = first letter of the row
	    if letterToDecode.isupper():      
	      decodedString += self.m[i][0].upper()
	    else:
	      decodedString += self.m[i][0]    
    return decodedString

if __name__ == '__main__':
  	
  stringToCrypt = sys.argv[1]
  key = sys.argv[2]
  	
  vig = Vigenere(stringToCrypt, key)
  stringCrypted = vig.cypher() 
  print "encrypt ", stringToCrypt, " => ", stringCrypted 

  vig = Vigenere(stringCrypted, key)
  print "decrypt ", stringCrypted, " => ", vig.decypher() 



