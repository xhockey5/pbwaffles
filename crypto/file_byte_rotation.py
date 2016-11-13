# Author - pbwaffles

data = open('testfile.txt', 'rb').read()
with open('outfile.txt', 'wb') as outfile:

    shift = 2 # shifts the bytes in a file by this amount (in decimal)
    newbytes = ''

    for byte in data:
        newbytes += (chr(ord(byte)+shift))

    outfile.write(newbytes)
