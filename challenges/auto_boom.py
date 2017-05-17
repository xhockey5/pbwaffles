from subprocess import Popen, PIPE
import os


answer1 = "The cold never bothered me anyway."
answer2 = "0 0 0 0 0 0"
answer3 = "0 w 1105"
answer4 = '12'
answer5 = 'ahdno'
answer6 = '\x00, \x00, \x00, \x00, \x00, \x00'

p = Popen('./NCL-2016-Post-BoomBoom', stdin=PIPE, stdout=PIPE) #NOTE: no shell=True here
out = p.communicate(input=os.linesep.join([answer1, answer2, answer3, answer4, answer5]))
print out
if 'Nice!' in out:
    print '*'*100
    print out
    print answer6
    print '*'*100
