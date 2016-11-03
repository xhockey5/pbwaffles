# Author - pbwaffles


# every possible symbol that can be encrypted
#LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(encrypted):
    """
    encryped is a string that contains the encrypted text in all uppercase characters.
    prints out decrpyted string using every shift (1-25).
    """
    for i in range(1,26):
        decrypted = ''
        for letter in encrypted:
            newLetter = chr(ord(letter)+i)
            #don't allow letter to go past 'Z', loops back to 'A'
            if ord(newLetter) > 90: # ord('Z') = 90
                newLetter = chr(ord(letter)+i-26) #loops to begin of alphabet
            decrypted += newLetter
        print 'Shift %i: %s' % (i, decrypted)
