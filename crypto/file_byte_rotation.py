data = open('testfile.txt', 'rb').read()
outfile = open('outfile.txt', 'wb')

shift = 2
newbytes = ''
for byte in data:
    newbytes += (chr(ord(byte)+shift))
outfile.write(newbytes)
outfile.close()
