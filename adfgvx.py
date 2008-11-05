#!/usr/bin/env python

# ADFGVX encryption/decryption importable class (buckminst)

import sys

class ADFGVX:
  def __init__(self, worktext, transposekey):
    self.base_alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    self.letter_key = ['a', 'd', 'f', 'g', 'v', 'x']
    self.alpha_key = [ ['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p', 'q', 'r'], ['s', 't', 'u', 'v', 'w', 'x'], ['y', 'z', '0', '1', '2', '3'], ['4', '5', '6', '7', '8', '9'] ]
    self.worktext = worktext
    self.transposekey = transposekey

  def encrypt(self):
    print "ADFGVX encryption subshell."
    print "Base Alphabet:",
    print self.base_alphabet
    print "\nBlock Cipher:"
    print "   ADFGVX"
    print "   ------"
    print "A|"
    print "".join(self.alpha_key[0])
    print "D|",
    print "".join(self.alpha_key[1])
    print "F|",
    print "".join(self.alpha_key[2])
    print "G|",
    print "".join(self.alpha_key[3])
    print "V|",
    print "".join(self.alpha_key[4])
    print "X|",
    print "".join(self.alpha_key[5])

    plain_string=self.worktext.lstrip().rstrip().lower()
    trans_string=self.transposekey.lstrip().rstrip().lower()

    print "Parsing input string..."

    key_string = ""
    for i in range(0,len(plain_string)):
      char_loc_c = 0
      char_loc_r = 0
      to_match = plain_string[i]
      for j in range(0, len(self.alpha_key)):
        try:
          char_loc_c = self.alpha_key[j].index(to_match)
          char_loc_r = j
          key_string = key_string + self.letter_key[char_loc_r] + self.letter_key[char_loc_c] + " "
        except ValueError:
          pass

    key_string = key_string.rstrip()

    key_string_list = key_string.split(" ")
    key_string_new = "".join(key_string_list)

    key_len = len(key_string_new)
    key_pos = 0

    for i in range(0,len(trans_string)):
      print trans_string[i],
    print
    print "- - - - - -"

    msg_block_c = list()
    while key_pos < key_len:
      cur_line = ""
      cur_list = list()
      for i in range(0,len(trans_string)):
        try:
          cur_line = cur_line + key_string_new[key_pos] + " "
          cur_list.append(key_string_new[key_pos])
        except IndexError:
          break
        key_pos = key_pos + 1
      cur_line = cur_line.rstrip()
      print cur_line
      msg_block_c.append(cur_list)

    trans_list = list()
    msg_block_d = dict()
    for i in range(0,len(trans_string)):
      cur_line = ""
      cur_list = list()
      for j in range(0,len(msg_block_c)):
        try:
          cur_line = cur_line + msg_block_c[j][i] + " "
          cur_list.append(msg_block_c[j][i])
        except IndexError:
          pass
      cur_line = cur_line.rstrip()
      trans_list.append(trans_string[i])
      msg_block_d[trans_string[i]] = cur_list

    trans_list.sort()
    sorted_string = "".join(trans_list)
    print
    for i in range(0,len(sorted_string)):
      print sorted_string[i],
    print
    print "- - - - - -"

    msg_block_t = list()
    for i in range(0,len(msg_block_c)):
      cur_line = ""
      cur_list = list()
      for j in range(0,len(sorted_string)):
        try:
          cur_line = cur_line + msg_block_d[sorted_string[j]][i] + " "
          cur_list.append(msg_block_d[sorted_string[j]][i])
        except IndexError:
          cur_line = cur_line + "  "
          cur_list.append(" ")
          pass
      print cur_line
      msg_block_t.append(cur_list)

    final_string = ""
    for i in range(0,len(sorted_string)):
      for j in range(0,len(msg_block_t)):
        if msg_block_t[j][i] != " ":
          try:
            final_string = final_string + msg_block_t[j][i]
          except IndexError:
            pass
      final_string = final_string + " "

    print 
    print "Encrypted message string is: " + final_string
    return final_string


  def decrypt(self):
    print "ADFGVX decryption subshell."
    print "Base Alphabet:",
    print self.base_alphabet
    print "\nBlock Cipher:"
    print "   ADFGVX"
    print "   ------"
    print "A|",
    print "".join(self.alpha_key[0])
    print "D|",
    print "".join(self.alpha_key[1])
    print "F|",
    print "".join(self.alpha_key[2])
    print "G|",
    print "".join(self.alpha_key[3])
    print "V|",
    print "".join(self.alpha_key[4])
    print "X|",
    print "".join(self.alpha_key[5])

    cypher_string=self.worktext.lstrip().rstrip().lower()
    trans_string=self.transposekey.lstrip().rstrip().lower()

    print "Decrypting..."
    cypher_list = cypher_string.split(" ")

    trans_list = list()
    sorted_list = list()
    for i in range(0, len(trans_string)):
      trans_list.append(trans_string[i])
      sorted_list.append(trans_string[i])
    sorted_list.sort()

    max_line_len = 0;
    for i in range(0, len(cypher_list)):
      if len(cypher_list[i]) > max_line_len: max_line_len = len(cypher_list[i])

    msg_block_d = dict()
    for i in range(0, len(trans_string)):
      cur_line = ""
      cur_list = list()
      for j in range(0, max_line_len):
        try:
          cur_list.append(cypher_list[i][j])
        except IndexError:
          cur_list.append(" ")
      msg_block_d[sorted_list[i]] = cur_list


    sorted_string = "".join(sorted_list)
    print
    for i in range(0,len(sorted_string)):
      print sorted_string[i],
    print
    print "- - - - - -"

    for i in range(0, max_line_len):
      cur_line = ""
      for j in range(0, len(sorted_string)):
        cur_line = cur_line + msg_block_d[sorted_string[j]][i] + " "
      print cur_line

    print
    for i in range(0,len(trans_string)):
      print trans_string[i],
    print
    print "- - - - - -"

    index_string = ""
    for i in range(0, max_line_len):
      cur_line = ""
      for j in range(0, len(trans_string)):
        cur_line = cur_line + msg_block_d[trans_string[j]][i] + " "
        index_string = index_string + msg_block_d[trans_string[j]][i]
      print cur_line
    index_string.rstrip()

    final_string = ""
    for i in range(0, len(index_string), 2):
      indexloc_a = 0
      indexloc_b = 0
      try:
        indexloc_a = self.letter_key.index(index_string[i])
        indexloc_b = self.letter_key.index(index_string[i+1])
        final_string = final_string + str(self.alpha_key[indexloc_a][indexloc_b])
      except ValueError:
        pass

    print
    print "Decrypted message string is: " + final_string
    return final_string

if __name__ == '__main__':
  textToHandle = sys.argv[1]
  transKey = sys.argv[2]

  myADFGVX = ADFGVX(textToHandle, transKey)
  cryptString = myADFGVX.encrypt()
  print "Encrypt: ", textToHandle, " -> ", cryptString
  
  myADFGVX = ADFGVX(cryptString, transKey)
  print "Decrypt: ", cryptString, " -> ", myADFGVX.decrypt()
