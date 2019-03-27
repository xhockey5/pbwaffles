from subprocess import Popen, PIPE
import os


answer1 = "The cold never bothered me anyway."
answer2 = "0 0 0 0 0 0"
answer3 = "0 w 1105"
answer4 = '12'
answer5 = 'ahdno'
answer6 = '4 6 3 2 5 1'

p = Popen('./NCL-2016-Post-BoomBoom', stdin=PIPE, stdout=PIPE) #NOTE: no shell=True here
answers = [answer1, answer2, answer3, answer4, answer5, answer6]
out = p.communicate(input=os.linesep.join(answers))
stdout = out[0].splitlines()

print '\n'.join(stdout)
