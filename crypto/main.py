import argparse
import ceasershift
import transpositionDecrypt



if __name__ == '__main__':

    #do stuff here
    parser = argparse.ArgumentParser(description='Decrypt encrypted text. Supports ceasershift, substitution, transposition, and vigenere.')
    parser.add_argument('-c', '--cipher', help='Choose which cipher to use', default='guess', choices=['ceaser', 'substitution', 'transposition', 'vigenere'])
    parser.add_argument('-e', '--encrypted', help='Encrypted text to decrypt')
    args = parser.parse_args()
    args = vars(args)
    encryptedText = args['encrypted'].upper()
    cipher = args['cipher']
    if cipher == 'ceaser':
        ceasershift.decrypt(encryptedText)
    elif cipher == 'substituition':
        print 'This doesnt exist yet'
    elif cipher == 'transposition':
        transpositionDecrypt.main(encryptedText)
        print 'not done yet'
    elif cipher == 'vigenere':
        #call vigenere cipher
        print 'not done yet'
