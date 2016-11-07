# Vigenere Cipher

import time

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def print_deciphered(key, encryptedString):
    decryptMessage(key, encryptedString)

def attempt_keys(message, bestKeys, keyWordList):
    with open(keyWordList, 'r') as f: #wordlist to try
        count = 0
        keyFound = False
        newBestKeys = bestKeys
        for myKey in f:
            count += 1
            if (count % 1000) == 0:
                print 'Attempt %i' % count
            myKey = myKey.strip('\n')
            translated = decryptMessage(myKey, message)
            if translated: #checks to make sure there is a decrypted message
                if translated[0] == 'C': #use this to specify location of a known plaintext character if known
                    score = is_english(translated)
                    if len(bestKeys) <= 10:
                        newBestKeys[myKey] = score
                    else:
                        for key in bestKeys:
                            if score > bestKeys[key]:
                                del newBestKeys[key]
                                newBestKeys[myKey] = score
                                break
                    for key in newBestKeys: #checks to see if the right key has been found based on if the score is high enough
                        if int(newBestKeys[key]) > 70: #50 is an arbitrary score number to guess at (don't know a good way to determine this)
                            keyFound = True
                    if keyFound:
                        return newBestKeys
    return newBestKeys

def is_english(decryptText):
    #this will check for words that are x letters or shorter
    f = open('dictionary.txt', 'r')
    englishWords = []
    for line in f:
        englishWords.append(line.strip('\n'))
    score = 0
    currentPos = 0
    for word in englishWords:
        if word in decryptText:
            score += 1
    f.close()
    return score

def main(myMessage='', keyWordList='/root/Desktop/rockyou.txt'):

    bestKeys = {}
    startTime = time.time()
    bestKeys = attempt_keys(myMessage, bestKeys, keyWordList)

    print 'the best keys are...\n'
    for key in bestKeys:
        print 'Key: %s' % key
        print 'Message: %s' % decryptMessage(key, myMessage)
    print '\n'
    endTime = time.time()
    hour = (endTime-startTime)/3600 #3600 seconds in an hour
    minute = ((endTime-startTime)/60) % 60 #60 seconds in a minute
    second = (endTime-startTime) % 60
    print 'Time elapsed: %i hour(s) %i minute(s) %i second(s)' % (hour, minute, second)

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    try:
        translated = [] # stores the encrypted/decrypted message string

        keyIndex = 0
        key = key.upper()

        for symbol in message: # loop through each character in message
            num = LETTERS.find(symbol.upper())
            if num != -1: # -1 means symbol.upper() was not found in LETTERS
                if mode == 'encrypt':
                    num += LETTERS.find(key[keyIndex]) # add if encrypting
                elif mode == 'decrypt':
                    num -= LETTERS.find(key[keyIndex]) # subtract if decrypting

                num %= len(LETTERS) # handle the potential wrap-around

                # add the encrypted/decrypted symbol to the end of translated.
                if symbol.isupper():
                    translated.append(LETTERS[num])
                elif symbol.islower():
                    translated.append(LETTERS[num].lower())

                keyIndex += 1 # move to the next letter in the key
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                # The symbol was not in LETTERS, so add it to translated as is.
                translated.append(symbol)

        return ''.join(translated)
    except IndexError:
        print 'There was an error'
        return ''


# If vigenereCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    myMessage = "YHTEQAPSSQWLTLSILYPENZIZSJLVPVIPVWLKDLZRCWZXGEZEWCDHDBRCSIEXHLWKRKTOYIUPVFCLBRDIWULGSPOIYKLHZMMYBLLVPVQGXAYEDXILWGWDVRPMPOWNKDAIHSQSLLEESAMSQAIEMPALPEJKAXIPOEHEPLZRTWYTZJPOMPSNSD"
    main(myMessage)
