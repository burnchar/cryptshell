# Introduction #

Enigma can be run in two modes, encryption or decryption.  There are some options for making ciphers more secure.  The first is to have your own key using the -k option The next is to use your own number of rotors using the -r option.  There is also an option to find what number of rotors was used if you know the key.  The code will check the use of 1-20 rotors using the -u option.  The following will walk through the process of doing each of these.

# Tutorial #

Enter the crypt shell with a file of your choice.

**$> cryptshell text.txt**

The cryptshell will start and you can check that your text was entered by typing:

**-> print current**

The text.txt file will print.
To encrypt the enigma cipher needs no arguments, but for this example we will set a key.

**-> enigma -k rocks**

It will return the number of rotors and what key was used.
You can print the current text to see what it was encrypted too.  This can be decrypted by typing:

**-> enigma -dk rocks**

If the -k is left off the encryption will not be done correctly and the text will be further scrambled.  It can be reversed but must be done in the reverse order of the original sequence with the proper keys.
Print the current text to see if you have the original text back.
Now lets use the rotor options.  The -r sets the number of rotors that are used.

**-> enigma -r 8**

and

**-> enigma -r 5**

Will give different encryptions.  Try both printing the results after each.  Remember to decrypt the text between each to do a proper comparison.

The -r and -k can be used together.

**-> enigma -k rocks -r 8**

If you remember the key but don't remember the number of rotors used.  The -u option will find possible completions for you.  It checks from 1 rotor to 20 looking at each possibility to see if they make english words.  It will return the first possible completion it finds that has better then 50% of the text in english.  It is used as follows:

**-> enigma -uk rocks**

The enigma program know that the -u is used only for decryption so the -d is not needed.