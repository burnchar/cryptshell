#!/usr/bin/env python

base_alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

letter_key = ['a', 'd', 'f', 'g', 'v', 'x']

alpha_key = [ ['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p', 'q', 'r'], ['s', 't', 'u', 'v', 'w', 'x'], ['y', 'z', '0', '1', '2', '3'], ['4', '5', '6', '7', '8', '9'] ]

print "ADFGVX decryption subshell."
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

cypher_string=raw_input("Input cypher string: ").lstrip().rstrip().lower()
trans_string=raw_input("Input transposition string: ").lstrip().rstrip().lower()

print "Decrypting..."
#print "Transposition string: " + trans_string
#print "Cypher Text: " + cypher_string
cypher_list = cypher_string.split(" ")
#print cypher_list

trans_list = list()
sorted_list = list()
for i in range(0, len(trans_string)):
  trans_list.append(trans_string[i])
  sorted_list.append(trans_string[i])
sorted_list.sort()
#print trans_list
#print sorted_list

max_line_len = 0;
for i in range(0, len(cypher_list)):
  if len(cypher_list[i]) > max_line_len: max_line_len = len(cypher_list[i])
#print "Max line length: " + str(max_line_len)

msg_block_d = dict()
for i in range(0, len(trans_string)):
  cur_line = ""
  cur_list = list()
  for j in range(0, max_line_len):
    try:
      cur_list.append(cypher_list[i][j])
    except IndexError:
      cur_list.append(" ")
#  print cur_list
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

#print
#print "Index string is: " + index_string
final_string = ""
for i in range(0, len(index_string), 2):
  indexloc_a = 0
  indexloc_b = 0
  try:
#    print str(index_string[i]) + str(index_string[i+1]),
#    print index_string[i] + " is: " + str(letter_key.index(index_string[i])),
#    print " & " + index_string[i+1] + " is: " + str(letter_key.index(index_string[i+1]))
    indexloc_a = letter_key.index(index_string[i])
    indexloc_b = letter_key.index(index_string[i+1])
#    print "Alpha key line is: " + str(alpha_key[indexloc_a])
#    print "Alpha entry is: " + str(alpha_key[indexloc_a][indexloc_b])
    final_string = final_string + str(alpha_key[indexloc_a][indexloc_b])
#    print "Final String is: " + final_string
  except ValueError:
    pass

print
print "Decrypted message string is: " + final_string
