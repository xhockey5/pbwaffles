# Author - pbwaffles

data = open('a.out', 'rb').read()
with open('outfile.txt', 'wb') as outfile:

    shift = 2 # shifts the bytes in a file by this amount (in decimal)
    newbytes = ''

    for byte in data:
        shit = (ord(byte) + shift)
        if (shit > 255):
            shit = shit % 256

        newbyte = chr(shit)
        newbytes += newbyte

    outfile.write(newbytes)
