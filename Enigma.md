# History/Introduction #

The Enigma cipher is based on a WWII cipher used by the Germans to send encrypted communications without the enemy understanding what was being said.  The encryption they used was based on three rotors that each had all the letters of the alphabet on them.  Each rotor did a simple substitution, but the rotors would move as the user would type.  The device had a key board that after each key was pushed one of the rotors would turn.  After the first rotor turned 360 degrees the next rotor would turn once.  Then after the second turned 360 degrees the third would increment once.  This cipher is similar but the user has the option to pick as many rotors as they want.  It uses a piece of code that use to be available in Python, but was removed for political reasons (see python documentation on the history of the rotor).  One of the developers converted the original code (C) to python where I am using it.  See the rotor.py file from the repository for complete details.

The Enigma cipher implemented here is similar to the enigma machine used in WWII, but the enigma machine uses a few other switches and tricks that are not implemented here.  The implementation here also allows as many rotors as you feel like putting.  This implementation will also figure out how many rotors you used (up to 20) if you don't remember, but it requires you to still know what your key is.  This could easily be expanded to use more rotors, or search a dictionary for keys, but this has not been done yet.

# Syntax #

>enigma -h

Usage: enigma [-e | --encrypt] | [-d | --decrypt] [-u | --unknown] [-h | --help] [-k | --key cipherKey] [-r | --rotor cipherRotorNumber]

> -e, --encrypt    Encrypt input.  Can not be used with the -d switch.

> -d, --decrypt    Decrypt input.  Can not be used with the -e switch.

> -u, --unknown    Unknown rotor number for the given encrypted input.

> ............... Note this option only is used for decryption it has

> ............... no effect if the -e or --encrypt switches are set.

> -k, --key        Set the key used to encrypt or decrypt an input (string).

> -r, --rotors     Set the number encryption/decryption rotors (int).

> -h, --help       Print this screen.

# EnigmaTutorial #