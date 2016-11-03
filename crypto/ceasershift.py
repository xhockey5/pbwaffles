# Caesar Cipher
# Adapted by Marc Friedenberg from http://inventwithpython.com/hacking (BSD Licensed)

import sys, detectEnglish

# every possible symbol that can be encrypted
#LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while 1:

    # the string to be encrypted/decrypted
    message = raw_input('What is your message? ')

    # tell the program to encrypt, decrypt, or hack
    mode = raw_input("Select a mode: ('e' to encrypt, 'd' to decrypt, 'h' to hack): ")
    if (mode == "e" or mode == "d"):
        while True:
            try:
                key = int(raw_input("Enter a key (must be an integer): "))
            except ValueError:
                print("Your key must be an integer.")
                continue
            else:
                break

        # stores the encrypted/decrypted form of the message
        translated = ''

        # run the encryption/decryption code on each symbol in the message string
        for symbol in message:
            if symbol in LETTERS:
                # get the encrypted (or decrypted) number for this symbol
                num = LETTERS.find(symbol) # get the number of the symbol
                if mode == 'e':
                    num = num + key
                elif mode == 'd':
                    num = num - key

                # handle the wrap-around if num is larger than the length of
                # LETTERS or less than 0
                if num >= len(LETTERS):
                    num = num - len(LETTERS)
                elif num < 0:
                    num = num + len(LETTERS)

                # add encrypted/decrypted number's symbol at the end of translated
                translated = translated + LETTERS[num]

            else:
                # just add the symbol without encrypting/decrypting
                translated = translated + symbol

        # print the encrypted/decrypted string to the screen
        print
        print(translated)

    elif (mode == "h"):
        for key in range(len(LETTERS)):

            # It is important to set translated to the blank string so that the
            # previous iteration's value for translated is cleared.
            translated = ''

            # run the encryption/decryption code on each symbol in the message
            for symbol in message:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol) # get the number of the symbol
                    num = num - key

                    # handle the wrap-around if num is 26 or larger or less than 0
                    if num < 0:
                        num = num + len(LETTERS)

                    # add number's symbol at the end of translated
                    translated = translated + LETTERS[num]

                else:
                    # just add the symbol without encrypting/decrypting
                    translated = translated + symbol

            # display the current key being tested, along with its decryption
            print('Key #%s: %s' % (key, translated))
            if detectEnglish.isEnglish(translated):
                # Check with user to see if the decrypted key has been found.
                print("***")
                print('Possible encryption hack:')
                print('Key %s: %s' % (key, translated))
                print("***")
    else:
        print "You have selected an improper option"
    print "\n*****************************************************************\n"
