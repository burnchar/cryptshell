#!/usr/bin/env python

base_alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

letter_key = ['a', 'd', 'f', 'g', 'v', 'x']

alpha_key = [ ['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p', 'q', 'r'], ['s', 't', 'u', 'v', 'w', 'x'], ['y', 'z', '0', '1', '2', '3'], ['4', '5', '6', '7', '8', '9'] ]

print "ADFGVX encryption subshell."
print "Base Alphabet:",
print base_alphabet
print "\nBlock Cipher:"
print "   ADFGVX"
print "   ------"
print "A|",
print "".join(alpha_key[0])
print "D|",
print "".join(alpha_key[1])
print "F|",
print "".join(alpha_key[2])
print "G|",
print "".join(alpha_key[3])
print "V|",
print "".join(alpha_key[4])
print "X|",
print "".join(alpha_key[5])

plain_string=raw_input("Input plaintext string: ").lstrip().rstrip().lower()
trans_string=raw_input("Input transposition string: ").lstrip().rstrip().lower()

print "Parsing input string..."

key_string = ""
for i in range(0,len(plain_string)):
#  ignore_flag = 0
  char_loc_c = 0
  char_loc_r = 0
  to_match = plain_string[i]
  for j in range(0, len(alpha_key)):
#    print "checking keyrow " + str(j) + ":" + "".join(alpha_key[j]) + " for " + to_match
    try:
      char_loc_c = alpha_key[j].index(to_match)
      char_loc_r = j
      key_string = key_string + letter_key[char_loc_r] + letter_key[char_loc_c] + " "
    except ValueError:
      pass
#  print "Location of " + to_match + " is " + letter_key[char_loc_r] + "" + letter_key[char_loc_c]
#  print "ignore flag is: " + str(ignore_flag)
#  key_string = key_string + letter_key[char_loc_r] + letter_key[char_loc_c] + " "

key_string = key_string.rstrip()
#print "Intermediate key string for message is: " + key_string

key_string_list = key_string.split(" ")
key_string_new = "".join(key_string_list)
#print key_string_new

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
#  print cur_list
  msg_block_c.append(cur_list)

#for i in range(0,len(msg_block_c)):
#  print msg_block_c[i]

#print len(msg_block_c)

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
#  print trans_string[i]
#  print cur_line
#  print cur_list
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

#print msg_block_t

#final_string = ""
#for i in range(0,len(msg_block_t)):
#  final_string = final_string + "".join(msg_block_t[i]) + " "

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
