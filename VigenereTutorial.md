# The vigenere cipher #


### Introduction ###

The Vigenere cipher is polyalphabetic substitution cipher. It uses a key to encrypt and decrypt alphabetic texts.

More information on [Wikipedia](http://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

### Syntax ###

Usage: vigenere [-e | --encrypt] | [-d | --decrypt] [-h | --help] [-k | --key cipherKey]

> -e, --encrypt Encrypt input. Can not be used with the -d switch.

> -d, --decrypt Decrypt input. Can not be used with the -e switch.

> -k, --key Set the key used to encrypt or decrypt an input (string).

> -h, --help Print this screen.


### Tutorial ###

Enter the crypt shell with a file of your choice.

**$> cryptshell text.txt**

The cryptshell will start and you can check that your text was entered by typing:

**-> print current**

To encrypt the file you need to provide a key of your choice and indicate the mode "encrypt".

**-> vigenere -k mykey -e**

You can print the current text to see what how it was encrypted.

**-> print current**

The file can be decrypted if the same key is used with the "decrypt" mode.

